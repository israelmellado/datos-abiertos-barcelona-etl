import streamlit as st

# ======================================
# PALETA CORPORATIVA
# ======================================
COLOR_PRIMARIO = "#0F4C5C"  # Azul petróleo
COLOR_SECUNDARIO = "#2C7A8C"
COLOR_FONDO = "#F7FBFC"  # <--- Este es el color que ahora sí se aplicará
COLOR_PANEL = "#EAF4F6"
COLOR_BORDE = "#D7E7EA"
COLOR_TEXTO = "#2F3B43"
COLOR_EXITO = "#2E8B57"
COLOR_AVISO = "#F4A261"
COLOR_ERROR = "#D1495B"


def aplicar_tema():
    """Aplica la hoja de estilos del dashboard anulando el fondo de Streamlit."""
    st.markdown(
        f"""
        <style>
        /* ===== Colores corporativos ===== */
        :root {{
            --primario: {COLOR_PRIMARIO};
            --secundario: {COLOR_SECUNDARIO};
            --fondo: {COLOR_FONDO};
            --panel: {COLOR_PANEL};
            --borde: {COLOR_BORDE};
            --texto: {COLOR_TEXTO};
        }}
        
        /* ===== SOLUCIÓN AL FONDO (Fuerza el color en la app de Streamlit) ===== */
        .stApp, .stAppHeader, div[data-testid="stAppViewContainer"] {{
            background-color: var(--fondo) !important;
        }}
        
        /* Asegura el color del texto global */
        .stApp p, .stApp span, .stApp label {{
            color: var(--texto);
        }}
        
        /* ===== Estructura del Sidebar ===== */
        section[data-testid="stSidebar"] {{
            background-color: var(--panel) !important;
            border-right: 1px solid var(--borde);
        }}
        
        /* ===== Tabs (Pestañas) ===== */

                div[data-baseweb="tab-list"]{{
            gap:12px;
        }}

        /* Todas las pestañas */
        button[data-testid="stTab"]{{
            background:var(--panel) !important;
            border:1px solid var(--borde) !important;
            border-radius:10px !important;
            padding:10px 18px !important;
            transition:.25s;
        }}

        /* Texto pestañas inactivas */
        button[data-testid="stTab"],
        button[data-testid="stTab"] p{{
            color:var(--primario) !important;
            -webkit-text-fill-color:var(--primario) !important;
        }}

        /* Hover */
        button[data-testid="stTab"]:hover{{
            background:#DCECEF !important;
        }}
        
        button[data-testid="stTab"] p{{
            color:var(--primario) !important;
        }}

        /* Activa */

        button[data-testid="stTab"][aria-selected="true"] p{{
            color:white !important;
        }}
        /* Activa */
        button[data-testid="stTab"][aria-selected="true"]{{
            background:var(--primario) !important;
            border-color:var(--primario) !important;
        }}
        /* Texto pestañas */

        button[data-testid="stTab"] p{{
            color:var(--primario) !important;
        }}
        
        /* Texto pestaña activa */
        
        button[data-testid="stTab"][aria-selected="true"]
        div[data-testid="stMarkdownContainer"] p{{
            color:#ffffff !important;
            -webkit-text-fill-color:#ffffff !important;
        }}
        /* ===== Títulos ===== */
        h1, h2, h3, h4, h5, h6 {{
            color: var(--primario) !important;
            font-weight: 700;
        }}
        
        /* ===== KPIs (st.metric) ===== */
        div[data-testid="stMetric"] {{
            background-color: white !important;
            border: 1px solid var(--borde) !important;
            border-left: 6px solid var(--primario) !important;
            border-radius: 12px;
            padding: 12px;
            min-height: 120px;
            transition: 0.2s;
            box-shadow: 0 3px 10px rgba(0,0,0,0.05);
        }}
        
        div[data-testid="stMetric"]:hover {{
            transform: translateY(-3px);
            box-shadow: 0 8px 18px rgba(0,0,0,.12);
        }}

        div[data-testid="stMetricLabel"] {{
            font-weight: 600;
            color: var(--secundario) !important;
        }}

        div[data-testid="stMetricValue"] {{
            color: var(--primario) !important;
            font-weight: 700;
        }}

        /* ===== Botones (st.button) ===== */
        div.stButton > button {{
            background-color: var(--primario) !important;
            color: white !important;
            border-radius: 8px;
            border: 1px solid var(--primario) !important;
            padding: 8px 16px;
            font-weight: 600;
            transition: 0.2s;
        }}

        div.stButton > button:hover {{
            background-color: var(--secundario) !important;
            border-color: var(--secundario) !important;
            color: white !important;
            transform: translateY(-1px);
        }}

        /* ===== Inputs y Selectores ===== */
        div[data-baseweb="select"], div[data-baseweb="input"] {{
            background-color: white !important;
            border-radius: 8px !important;
        }}
        
        div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {{
            border-color: var(--borde) !important;
        }}
        
        div[data-baseweb="select"]:focus-within, 
        div[data-baseweb="input"]:focus-within {{
            border: 1px solid var(--primario) !important;
            box-shadow: 0 0 0 1px var(--primario) !important;
        }}

        label[data-testid="stWidgetLabel"] p {{
            color: var(--texto) !important;
            font-weight: 600 !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
