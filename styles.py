import streamlit as st


def apply_styles() -> None:
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
