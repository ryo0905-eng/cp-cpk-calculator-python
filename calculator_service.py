from __future__ import annotations

from io import StringIO

import pandas as pd
import plotly.io as pio

from analysis import calculate_capability, interpret_results, make_histogram, recommendation_text
from sample_catalog import get_sample_series

DEFAULT_FORM = {
    "input_mode": "upload",
    "sample_key": "good",
    "usl": "10",
    "lsl": "0",
}

CALCULATOR_PAGE = {
    "page_title": "Cp / Cpk Calculator for Process Capability Analysis",
    "meta_description": "Free Cp and Cpk calculator with CSV upload, sample data, interpretation, and practical guidance for manufacturing and quality engineers.",
}


def parse_numeric_series(uploaded_file) -> pd.Series | None:
    if uploaded_file is None or uploaded_file.filename == "":
        return None

    df = pd.read_csv(StringIO(uploaded_file.stream.read().decode("utf-8-sig")))
    if df.empty:
        return None

    first_col = df.columns[0]
    return pd.to_numeric(df[first_col], errors="coerce").dropna()


def get_form_state(form_data) -> dict:
    return {
        "input_mode": form_data.get("input_mode", DEFAULT_FORM["input_mode"]),
        "sample_key": form_data.get("sample_key", DEFAULT_FORM["sample_key"]),
        "usl": form_data.get("usl", DEFAULT_FORM["usl"]),
        "lsl": form_data.get("lsl", DEFAULT_FORM["lsl"]),
    }


def build_initial_calculator_state() -> dict:
    return {
        "form": DEFAULT_FORM.copy(),
        "results": None,
        "status": None,
        "recommendations": [],
        "chart_html": None,
        "raw_values": [],
        "error_message": None,
    }


def run_calculation(form: dict, uploaded_file) -> dict:
    usl = float(form["usl"])
    lsl = float(form["lsl"])
    if usl <= lsl:
        raise ValueError("USL must be greater than LSL.")

    if form["input_mode"] == "sample":
        data = get_sample_series(form["sample_key"])
    else:
        data = parse_numeric_series(uploaded_file)

    if data is None or len(data) == 0:
        raise ValueError("Provide a CSV with numeric values or choose a sample dataset.")
    if len(data) < 2:
        raise ValueError("Please provide at least 2 numeric values.")

    results = calculate_capability(data, usl, lsl)
    status_title, status_message, status_level = interpret_results(results["cp"], results["cpk"])

    return {
        "results": results,
        "status": {
            "title": status_title,
            "message": status_message,
            "level": status_level,
        },
        "recommendations": recommendation_text(results["cp"], results["cpk"]),
        "chart_html": pio.to_html(
            make_histogram(data, usl, lsl),
            full_html=False,
            include_plotlyjs="cdn",
            config={"displayModeBar": False, "responsive": True},
        ),
        "raw_values": [float(value) for value in data.tolist()],
    }
