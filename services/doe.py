from __future__ import annotations

import csv
import io
import random
from itertools import product


DOE_PAGE = {
    "page_title": "DoE Planner | Free Orthogonal Array and Factorial Generator",
    "meta_description": "Create a free DoE planning table with orthogonal arrays or full factorial runs. Set factor names, choose levels, randomize run order, and export the plan as CSV.",
}

MAX_FACTORS = 5
DEFAULT_FACTOR_COUNT = 3
DEFAULT_DESIGN_TYPE = "orthogonal_auto"

DESIGN_OPTIONS = [
    {"value": "orthogonal_auto", "label": "Orthogonal array (Auto)"},
    {"value": "orthogonal_l4", "label": "Orthogonal array L4"},
    {"value": "orthogonal_l8", "label": "Orthogonal array L8"},
    {"value": "orthogonal_l16", "label": "Orthogonal array L16"},
    {"value": "full_factorial", "label": "Full factorial"},
]

ORTHOGONAL_ARRAY_DEFINITIONS = {
    "orthogonal_l4": {"label": "Orthogonal array L4", "base_columns": 2, "max_factors": 3},
    "orthogonal_l8": {"label": "Orthogonal array L8", "base_columns": 3, "max_factors": 7},
    "orthogonal_l16": {"label": "Orthogonal array L16", "base_columns": 4, "max_factors": 15},
}


def _default_factor(index: int) -> dict:
    return {
        "name": f"Factor {index}",
        "low": "Low",
        "high": "High",
    }


def build_initial_doe_state() -> dict:
    form = {
        "factor_count": DEFAULT_FACTOR_COUNT,
        "randomize": True,
        "design_type": DEFAULT_DESIGN_TYPE,
    }
    factors = []

    for index in range(1, MAX_FACTORS + 1):
        factor = _default_factor(index)
        form[f"factor_{index}_name"] = factor["name"]
        form[f"factor_{index}_low"] = factor["low"]
        form[f"factor_{index}_high"] = factor["high"]
        factors.append({"index": index, **factor})

    state = {
        "form": form,
        "factor_fields": factors,
        "table": [],
        "csv_content": "",
        "summary": None,
        "error_message": None,
        "design_options": DESIGN_OPTIONS,
    }

    try:
        state.update(build_doe_plan(form))
    except Exception as exc:
        state["error_message"] = str(exc)

    return state


def get_doe_form_state(form_data) -> tuple[dict, list[dict]]:
    try:
        factor_count = int(form_data.get("factor_count", DEFAULT_FACTOR_COUNT))
    except (TypeError, ValueError):
        factor_count = DEFAULT_FACTOR_COUNT

    factor_count = max(2, min(MAX_FACTORS, factor_count))

    design_type = form_data.get("design_type", DEFAULT_DESIGN_TYPE)
    valid_design_types = {option["value"] for option in DESIGN_OPTIONS}
    if design_type not in valid_design_types:
        design_type = DEFAULT_DESIGN_TYPE

    form = {
        "factor_count": factor_count,
        "randomize": form_data.get("randomize") == "on",
        "design_type": design_type,
    }
    factors = []

    for index in range(1, MAX_FACTORS + 1):
        default_factor = _default_factor(index)
        name = (form_data.get(f"factor_{index}_name") or default_factor["name"]).strip()
        low = (form_data.get(f"factor_{index}_low") or default_factor["low"]).strip()
        high = (form_data.get(f"factor_{index}_high") or default_factor["high"]).strip()

        form[f"factor_{index}_name"] = name
        form[f"factor_{index}_low"] = low
        form[f"factor_{index}_high"] = high
        factors.append(
            {
                "index": index,
                "name": name,
                "low": low,
                "high": high,
            }
        )

    return form, factors


def _build_active_factors(form: dict) -> list[dict]:
    factor_count = int(form["factor_count"])
    active_factors = []

    for index in range(1, factor_count + 1):
        name = form[f"factor_{index}_name"].strip() or f"Factor {index}"
        low = form[f"factor_{index}_low"].strip() or "Low"
        high = form[f"factor_{index}_high"].strip() or "High"
        active_factors.append(
            {
                "index": index,
                "name": name,
                "low": low,
                "high": high,
            }
        )

    names = [factor["name"].lower() for factor in active_factors]
    if len(names) != len(set(names)):
        raise ValueError("Use unique factor names so the plan is easy to read.")

    return active_factors


def _build_full_factorial_rows(active_factors: list[dict]) -> list[dict]:
    rows = []
    for standard_order, levels in enumerate(product([0, 1], repeat=len(active_factors)), start=1):
        row = {
            "standard_order": standard_order,
            "settings": [],
        }
        for factor, level in zip(active_factors, levels):
            coded_level = -1 if level == 0 else 1
            actual_level = factor["low"] if coded_level == -1 else factor["high"]
            row["settings"].append(
                {
                    "name": factor["name"],
                    "coded": coded_level,
                    "actual": actual_level,
                }
            )
        rows.append(row)
    return rows


def _generate_orthogonal_columns(base_columns: int) -> list[list[int]]:
    base_patterns = list(product([-1, 1], repeat=base_columns))
    columns = []

    for mask in range(1, 2**base_columns):
        column = []
        for row in base_patterns:
            value = 1
            for bit_index in range(base_columns):
                if mask & (1 << bit_index):
                    value *= row[bit_index]
            column.append(value)
        columns.append(column)

    return columns


def _resolve_design_type(design_type: str, factor_count: int) -> tuple[str, str]:
    if design_type == "full_factorial":
        return "full_factorial", "Full factorial"

    if design_type == "orthogonal_auto":
        if factor_count <= 3:
            return "orthogonal_l4", ORTHOGONAL_ARRAY_DEFINITIONS["orthogonal_l4"]["label"]
        if factor_count <= 5:
            return "orthogonal_l8", ORTHOGONAL_ARRAY_DEFINITIONS["orthogonal_l8"]["label"]
        return "orthogonal_l16", ORTHOGONAL_ARRAY_DEFINITIONS["orthogonal_l16"]["label"]

    definition = ORTHOGONAL_ARRAY_DEFINITIONS.get(design_type)
    if definition is None:
        raise ValueError("Unsupported design type.")

    if factor_count > definition["max_factors"]:
        raise ValueError(f"{definition['label']} supports up to {definition['max_factors']} factors.")

    return design_type, definition["label"]


def _build_orthogonal_rows(active_factors: list[dict], design_type: str) -> list[dict]:
    definition = ORTHOGONAL_ARRAY_DEFINITIONS[design_type]
    columns = _generate_orthogonal_columns(definition["base_columns"])
    rows = []
    run_count = len(columns[0])

    for row_index in range(run_count):
        row = {
            "standard_order": row_index + 1,
            "settings": [],
        }
        for factor_index, factor in enumerate(active_factors):
            coded_level = columns[factor_index][row_index]
            actual_level = factor["low"] if coded_level == -1 else factor["high"]
            row["settings"].append(
                {
                    "name": factor["name"],
                    "coded": coded_level,
                    "actual": actual_level,
                }
            )
        rows.append(row)

    return rows


def _apply_run_order(rows: list[dict], randomize: bool) -> list[dict]:
    ordered_rows = list(rows)
    if randomize:
        random.shuffle(ordered_rows)

    finalized_rows = []
    for run_order, row in enumerate(ordered_rows, start=1):
        finalized_rows.append(
            {
                "run_order": run_order,
                "standard_order": row["standard_order"],
                "settings": row["settings"],
            }
        )
    return finalized_rows


def build_doe_plan(form: dict) -> dict:
    active_factors = _build_active_factors(form)
    resolved_design_type, design_label = _resolve_design_type(form["design_type"], len(active_factors))

    if resolved_design_type == "full_factorial":
        rows = _build_full_factorial_rows(active_factors)
        design_notes = "Captures all runs for the selected factors. Best when factor count is low and interaction detail matters."
    else:
        rows = _build_orthogonal_rows(active_factors, resolved_design_type)
        design_notes = "Uses an orthogonal screening matrix to cut run count while keeping balanced main-effect coverage."

    randomized_rows = _apply_run_order(rows, randomize=bool(form["randomize"]))

    csv_buffer = io.StringIO()
    csv_writer = csv.writer(csv_buffer)
    csv_writer.writerow(["Design", design_label])
    csv_writer.writerow(["Factors", len(active_factors)])
    csv_writer.writerow(["Randomized", "Yes" if form["randomize"] else "No"])
    csv_writer.writerow([])

    header = ["Run order", "Standard order"]
    header.extend(factor["name"] for factor in active_factors)
    header.extend(f"{factor['name']} coded" for factor in active_factors)
    header.append("Response")
    csv_writer.writerow(header)

    table = []
    for row in randomized_rows:
        actual_values = [setting["actual"] for setting in row["settings"]]
        coded_values = [setting["coded"] for setting in row["settings"]]
        csv_writer.writerow([row["run_order"], row["standard_order"], *actual_values, *coded_values, ""])
        table.append(
            {
                "run_order": row["run_order"],
                "standard_order": row["standard_order"],
                "actual_values": actual_values,
                "coded_values": coded_values,
            }
        )

    return {
        "table": table,
        "csv_content": csv_buffer.getvalue(),
        "summary": {
            "factor_count": len(active_factors),
            "run_count": len(table),
            "randomized": bool(form["randomize"]),
            "factor_names": [factor["name"] for factor in active_factors],
            "design_type": resolved_design_type,
            "design_label": design_label,
            "design_notes": design_notes,
        },
        "active_factors": active_factors,
        "design_options": DESIGN_OPTIONS,
    }
