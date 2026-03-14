import pandas as pd
import streamlit as st

from analysis import make_histogram
from sample_data import GOOD_SAMPLE, HIGH_VAR_SAMPLE, SHIFTED_SAMPLE, build_sample_csv


def render_hero() -> None:
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


def metric_card(label: str, value: str) -> None:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar() -> tuple[str, object, str | None, float, float]:
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

    return input_mode, uploaded_file, selected_sample, usl, lsl


def load_data(input_mode: str, uploaded_file, selected_sample: str | None) -> pd.Series | None:
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

    return data


def render_summary(results: dict) -> None:
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


def render_status(status_title: str, status_message: str, status_level: str) -> None:
    if status_level == "error":
        st.error(f"**{status_title}**\n\n{status_message}")
    elif status_level == "warning":
        st.warning(f"**{status_title}**\n\n{status_message}")
    else:
        st.success(f"**{status_title}**\n\n{status_message}")


def render_main_layout(
    data: pd.Series,
    usl: float,
    lsl: float,
    status_title: str,
    status_message: str,
    recommendations: list[str],
) -> None:
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


def render_details(data: pd.Series) -> None:
    with st.expander("Show raw data"):
        st.dataframe(pd.DataFrame({"value": data}), use_container_width=True)

    with st.expander("Show formula reference"):
        st.write("Cp = (USL - LSL) / (6σ)")
        st.write("CPU = (USL - Mean) / (3σ)")
        st.write("CPL = (Mean - LSL) / (3σ)")
        st.write("Cpk = min(CPU, CPL)")


def render_footer() -> None:
    st.markdown("---")
    st.subheader("Need more advanced analysis?")
    st.write("Possible next features:")
    st.write("- Pp / Ppk")
    st.write("- Capability plot")
    st.write("- PDF report")
    st.write("- Multiple column analysis")

    st.write(
        "I'm building tools for quality and manufacturing engineers. "
        "Your feedback helps decide what features to build next."
    )

    st.link_button(
        "Give feedback (30 seconds)",
        "https://forms.gle/2sQdwEbdmH4JPKjD7"
    )