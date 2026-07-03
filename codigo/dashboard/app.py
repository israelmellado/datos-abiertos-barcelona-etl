import streamlit as st

st.set_page_config(
    page_title="Barcelona Open Data ETL",
    page_icon="🏗️",
    layout="wide",
)

st.title("🏗️ Barcelona Open Data ETL")

st.markdown(
    """
Dashboard interactivo construido a partir del pipeline ETL del proyecto.

Permite explorar las obras públicas del Ayuntamiento de Barcelona.
"""
)
