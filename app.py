import streamlit as st
from analysis import calculate_capability, interpret_results, recommendation_text
from styles import apply_styles
from ui import (
    load_data,
    render_details,
    render_hero,
    render_main_layout,
    render_sidebar,
    render_status,
    render_summary,
)


st.set_page_config(
    page_title="Cp / Cpk Calculator",
    page_icon="📊",
    layout="wide",
)

apply_styles()
render_hero()

input_mode, uploaded_file, selected_sample, usl, lsl = render_sidebar()
data = load_data(input_mode, uploaded_file, selected_sample)


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
    render_summary(results)
    render_status(status_title, status_message, status_level)
    render_main_layout(data, usl, lsl, status_title, status_message, recommendations)
    render_details(data)

except Exception as e:
    st.error(f"An error occurred: {e}")
