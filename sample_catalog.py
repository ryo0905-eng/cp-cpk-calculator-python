from __future__ import annotations

from io import BytesIO

from sample_data import GOOD_SAMPLE, HIGH_VAR_SAMPLE, SHIFTED_SAMPLE, build_sample_csv


SAMPLE_OPTIONS = {
    "good": {
        "label": "Good process",
        "values": GOOD_SAMPLE,
        "filename": "good_process.csv",
    },
    "shifted": {
        "label": "Shifted process",
        "values": SHIFTED_SAMPLE,
        "filename": "shifted_process.csv",
    },
    "high-variation": {
        "label": "High variation",
        "values": HIGH_VAR_SAMPLE,
        "filename": "high_variation.csv",
    },
}


def get_sample_series(sample_key: str | None) -> pd.Series | None:
    import pandas as pd

    if not sample_key or sample_key not in SAMPLE_OPTIONS:
        return None
    return pd.Series(SAMPLE_OPTIONS[sample_key]["values"])


def build_sample_file(sample_key: str) -> tuple[BytesIO, str] | None:
    sample = SAMPLE_OPTIONS.get(sample_key)
    if sample is None:
        return None

    csv_bytes = build_sample_csv(sample["values"]).encode("utf-8")
    return BytesIO(csv_bytes), sample["filename"]
