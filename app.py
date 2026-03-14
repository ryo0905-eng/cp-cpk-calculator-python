import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="Cp / Cpk Calculator",
    page_icon="📊",
    layout="wide",
)

# ---------- Custom CSS ----------
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    .hero-box {
        padding: 1.2rem 1.4rem;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
        margin-bottom: 1rem;
    }
    .hero-title {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }
    .hero-sub {
        color: #475569;
        font-size: 1rem;
        margin-bottom: 0.2rem;
    }
    .metric-card {
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 1rem;
        background: #ffffff;
        min-height: 110px;
    }
    .metric-label {
        color: #64748b;
        font-size: 0.9rem;
        margin-bottom: 0.35rem;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        line-height: 1.1;
    }
    .section-card {
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 1rem 1rem 0.6rem 1rem;
        background: #ffffff;
        margin-bottom: 1rem;
    }
    .small-note {
        color: #64748b;
        font-size: 0.9rem;
    }
    .pro-box {
        border: 1px dashed #94a3b8;
        border-radius: 14px;
        padding: 1rem 1rem 0.8rem 1rem;
        background: #f8fafc;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------- Sample Data ----------
GOOD_SAMPLE = [
    5.1, 5.0, 5.2, 4.9, 5.1, 5.0, 5.2, 4.8, 5.1, 5.0,
    5.2, 5.1, 5.0, 5.1, 5.2, 4.9, 5.1, 5.0, 5.2, 5.1,
]

SHIFTED_SAMPLE = [
    7.5, 7.6, 7.4, 7.7, 7.5, 7.6, 7.4, 7.8, 7.5, 7.6,
    7.4, 7.7, 7.5, 7.6, 7.4, 7.8, 7.5, 7.6, 7.4, 7.7,
]

HIGH_VAR_SAMPLE = [
    1.2, 8.5, 3.4, 6.7, 2.3, 9.1, 4.8, 7.9, 1.5, 8.2,
    3.7, 6.4, 2.9, 9.0, 4.1, 7.6, 1.8, 8.7, 3.2, 6.9,
]


def build_sample_csv(values: list[float]) -> str:
    rows = ["value"] + [str(v) for v in values]
    return "\n".join(rows)


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


def metric_card(label: str, value: str):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------- Hero ----------
st.markdown(
    """
    <div class="hero-box">
        <div class="hero-title">Cp / Cpk Calculator</div>
        <div class="hero-sub">
            Simple process capability analysis for quality and manufacturing engineers.
        </div>
        <div class="small-note">
            Upload a CSV, enter LSL and USL, and get instant capability metrics with a practical interpretation.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- Sidebar ----------
with st.sidebar:
    st.header("Input")

    input_mode = st.radio(
        "Data source",
        ["Upload CSV", "Use sample data"],
        index=0,
    )

    selected_sample = None
    uploaded_file = None

    if input_mode == "Upload CSV":
        uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
        st.caption("Use a CSV where the first column contains measurement values.")
    else:
        selected_sample = st.selectbox(
            "Choose a sample",
            ["Good process", "Shifted process", "High variation"],
        )

    st.markdown("### Specification limits")
    usl = st.number_input("USL", value=10.0, step=0.1)
    lsl = st.number_input("LSL", value=0.0, step=0.1)

    st.markdown("### Download sample CSVs")
    st.download_button(
        "good_process.csv",
        data=build_sample_csv(GOOD_SAMPLE),
        file_name="good_process.csv",
        mime="text/csv",
    )
    st.download_button(
        "shifted_process.csv",
        data=build_sample_csv(SHIFTED_SAMPLE),
        file_name="shifted_process.csv",
        mime="text/csv",
    )
    st.download_button(
        "high_variation.csv",
        data=build_sample_csv(HIGH_VAR_SAMPLE),
        file_name="high_variation.csv",
        mime="text/csv",
    )

    st.markdown("---")
    st.caption("Tip: Sample data makes the app feel usable immediately.")


# ---------- Load Data ----------
data = None

if input_mode == "Upload CSV":
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            if not df.empty:
                first_col = df.columns[0]
                data = pd.to_numeric(df[first_col], errors="coerce").dropna()
        except Exception as e:
            st.error(f"Could not read CSV: {e}")
else:
    if selected_sample == "Good process":
        data = pd.Series(GOOD_SAMPLE)
    elif selected_sample == "Shifted process":
        data = pd.Series(SHIFTED_SAMPLE)
    elif selected_sample == "High variation":
        data = pd.Series(HIGH_VAR_SAMPLE)


if data is None:
    st.info("Start by uploading a CSV or choosing a sample dataset from the sidebar.")
    st.stop()

if len(data) < 2:
    st.error("Please provide at least 2 numeric values.")
    st.stop()

if usl <= lsl:
    st.error("USL must be greater than LSL.")
    st.stop()

try:
    results = calculate_capability(data, usl, lsl)
    status_title, status_message, status_level = interpret_results(results["cp"], results["cpk"])
    recommendations = recommendation_text(results["cp"], results["cpk"])

    # ---------- Summary ----------
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("Summary")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("Sample Size", f"{results['n']}")
    with c2:
        metric_card("Mean", f"{results['mean']:.4f}")
    with c3:
        metric_card("Std Dev", f"{results['std']:.4f}")
    with c4:
        metric_card("Cp", f"{results['cp']:.3f}")

    c5, c6, c7 = st.columns(3)
    with c5:
        metric_card("CPU", f"{results['cpu']:.3f}")
    with c6:
        metric_card("CPL", f"{results['cpl']:.3f}")
    with c7:
        metric_card("Cpk", f"{results['cpk']:.3f}")
    st.markdown("</div>", unsafe_allow_html=True)

    # ---------- Status ----------
    if status_level == "error":
        st.error(f"**{status_title}**\n\n{status_message}")
    elif status_level == "warning":
        st.warning(f"**{status_title}**\n\n{status_message}")
    else:
        st.success(f"**{status_title}**\n\n{status_message}")

    # ---------- Main Layout ----------
    left, right = st.columns([1.8, 1.0])

    with left:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        fig = make_histogram(data, usl, lsl)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.subheader("Interpretation")
        st.write(f"**Capability status:** {status_title}")
        st.write(status_message)

        st.markdown("**Recommended next checks**")
        for item in recommendations:
            st.write(f"- {item}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(
            """
            <div class="pro-box">
                <h4 style="margin-top:0;">Pro version idea</h4>
                <div class="small-note" style="margin-bottom:0.6rem;">
                    This box helps users understand what advanced features could unlock.
                </div>
                <ul style="margin-top:0.2rem;">
                    <li>Pp / Ppk</li>
                    <li>Capability report PDF</li>
                    <li>Multiple column analysis</li>
                    <li>Capability plot</li>
                    <li>Saved projects</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ---------- Details ----------
    with st.expander("Show raw data"):
        st.dataframe(pd.DataFrame({"value": data}), use_container_width=True)

    with st.expander("Show formula reference"):
        st.write("Cp = (USL - LSL) / (6σ)")
        st.write("CPU = (USL - Mean) / (3σ)")
        st.write("CPL = (Mean - LSL) / (3σ)")
        st.write("Cpk = min(CPU, CPL)")

except Exception as e:
    st.error(f"An error occurred: {e}")