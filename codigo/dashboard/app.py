import sqlite3
import sys
from pathlib import Path

import geopandas as gpd
import pandas as pd
import plotly.express as px
import streamlit as st
from shapely import wkt

RAIZ_PROYECTO = Path(__file__).resolve().parents[2]
sys.path.append(str(RAIZ_PROYECTO))

from codigo.configuracion.config import BASE_DATOS

st.set_page_config(
    page_title="Barcelona Open Data ETL",
    page_icon="🏗️",
    layout="wide",
)

# ===============================
# Cargar datos
# ===============================

conexion = sqlite3.connect(BASE_DATOS)

df = pd.read_sql(
    "SELECT * FROM obras",
    conexion,
)

conexion.close()

# ===============================
# Título
# ===============================

st.title("🏗️ Barcelona Open Data ETL")

st.markdown(
    """
Dashboard interactivo construido a partir del pipeline ETL del proyecto.

Permite explorar las obras públicas del Ayuntamiento de Barcelona.
"""
)

st.divider()

# ===============================
# Sidebar
# ===============================

st.sidebar.header("Filtros")

distritos = sorted(df["distrito"].dropna().unique())

distrito = st.sidebar.selectbox(
    "Distrito",
    ["Todos"] + distritos,
)

if distrito != "Todos":
    df = df[df["distrito"] == distrito]

estados = sorted(df["estado"].dropna().unique())

estado = st.sidebar.selectbox(
    "Estado",
    ["Todos"] + estados,
)

if estado != "Todos":
    df = df[df["estado"] == estado]

tipos = sorted(df["tipo_obra"].dropna().unique())

tipo = st.sidebar.selectbox(
    "Tipo de obra",
    ["Todos"] + tipos,
)

if tipo != "Todos":
    df = df[df["tipo_obra"] == tipo]

# ===============================
# Geometría para el mapa
# ===============================

gdf = gpd.GeoDataFrame(
    df.copy(),
    geometry=df["geometria_wgs84"].apply(wkt.loads),
    crs="EPSG:4326",
)

# Calcular centroides de forma correcta
gdf_utm = gdf.to_crs(epsg=25831)

gdf["lon"] = gdf_utm.centroid.to_crs(epsg=4326).x
gdf["lat"] = gdf_utm.centroid.to_crs(epsg=4326).y

# ===============================
# KPIs
# ===============================

total_obras = len(df)
total_distritos = df["distrito"].nunique()
presupuesto_total = df["presupuesto_licitacion"].sum()
duracion_media = df["duracion_dias"].mean()

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric("Obras", f"{total_obras:,}")
kpi2.metric("Distritos", total_distritos)
kpi3.metric("Presupuesto", f"{presupuesto_total:,.0f} €")
kpi4.metric("Duración media", f"{duracion_media:.0f} días")

# ===============================
# Datos para gráficos
# ===============================

obras_distrito = (
    df.groupby("distrito")
    .size()
    .reset_index(name="obras")
    .sort_values("obras", ascending=False)
)

estado_df = df.groupby("estado").size().reset_index(name="obras")

fig_distritos = px.bar(
    obras_distrito,
    x="distrito",
    y="obras",
    title="Número de obras por distrito",
)

fig_estado = px.pie(
    estado_df,
    names="estado",
    values="obras",
    title="Distribución de las obras por estado",
)

# ===============================
# Gráficos
# ===============================

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        fig_distritos,
        width="stretch",
        key="grafico_distritos",
    )

with col2:
    st.plotly_chart(
        fig_estado,
        width="stretch",
        key="grafico_estado",
    )

# ===============================
# Mapa interactivo
# ===============================

st.subheader("Mapa de obras")

fig_mapa = px.scatter_map(
    gdf,
    lat="lat",
    lon="lon",
    color="estado",
    hover_name="tipo_obra",
    hover_data=[
        "distrito",
        "constructor",
        "duracion_dias",
    ],
    zoom=11,
    height=650,
)

st.plotly_chart(
    fig_mapa,
    width="stretch",
    key="mapa_obras",
)

# ===============================
# Tabla
# ===============================

st.subheader("Datos")

st.dataframe(
    df,
    width="stretch",
)
