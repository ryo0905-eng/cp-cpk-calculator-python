import numpy as np
import pandas as pd
import plotly.express as px


def calculate_capability(data: pd.Series, usl: float, lsl: float) -> dict:
    mean = float(np.mean(data))
    std = float(np.std(data, ddof=1))

    if std == 0:
        raise ValueError("Standard deviation is 0. Capability cannot be calculated.")

    cp = (usl - lsl) / (6 * std)
    cpu = (usl - mean) / (3 * std)
    cpl = (mean - lsl) / (3 * std)
    cpk = min(cpu, cpl)

    return {
        "n": int(len(data)),
        "mean": mean,
        "std": std,
        "cp": cp,
        "cpu": cpu,
        "cpl": cpl,
        "cpk": cpk,
    }


def interpret_results(cp: float, cpk: float) -> tuple[str, str, str]:
    if cpk < 1.0:
        if cp >= 1.33:
            return (
                "Off-center process",
                "Variation is relatively small, but the process mean is shifted toward one spec limit.",
                "error",
            )
        return (
            "Process not capable",
            "Process variation is too large for the current specification width.",
            "error",
        )
    if cpk < 1.33:
        return (
            "Marginal capability",
            "The process may meet specs now, but capability is not yet strong enough for stable operation.",
            "warning",
        )
    return (
        "Process capable",
        "The process appears capable for the current specification limits.",
        "success",
    )


def recommendation_text(cp: float, cpk: float) -> list[str]:
    if cp >= 1.33 and cpk < 1.0:
        return [
            "Check whether the process target is shifted from the nominal center.",
            "Review setup offsets, machine adjustment, or calibration.",
            "Compare recent lots or raw material changes.",
        ]
    if cp < 1.0:
        return [
            "Investigate sources of variation: machine, material, method, and measurement.",
            "Split the data by machine, shift, lot, or operator.",
            "Confirm measurement system stability before changing the process.",
        ]
    if cpk < 1.33:
        return [
            "Monitor the process more closely before judging it stable.",
            "Consider tightening centering and reducing special-cause variation.",
            "Review whether the current process target is appropriate.",
        ]
    return [
        "Continue routine monitoring.",
        "Confirm capability with time-based data and control charts.",
        "Keep tracking changes in process conditions and incoming material.",
    ]


def make_histogram(data: pd.Series, usl: float, lsl: float):
    mean_val = float(np.mean(data))
    fig = px.histogram(
        x=data,
        nbins=20,
        labels={"x": "Value", "y": "Count"},
        title="Distribution",
    )
    fig.add_vline(x=lsl, line_dash="dash", annotation_text="LSL", annotation_position="top left")
    fig.add_vline(x=usl, line_dash="dash", annotation_text="USL", annotation_position="top right")
    fig.add_vline(x=mean_val, line_dash="dot", annotation_text="Mean", annotation_position="top")

    fig.update_layout(
        height=440,
        bargap=0.05,
        xaxis_title="Measured Value",
        yaxis_title="Count",
        title_x=0.02,
        margin=dict(l=20, r=20, t=60, b=20),
    )
    return fig
