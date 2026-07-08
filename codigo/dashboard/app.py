import sys
from datetime import datetime
from pathlib import Path

import pandas as pd
import streamlit as st

RAIZ_PROYECTO = Path(__file__).resolve().parents[2]
sys.path.append(str(RAIZ_PROYECTO))

from codigo.dashboard.datos import cargar_datos
from codigo.dashboard.filtros import aplicar_filtros
from codigo.dashboard.graficos import (
    grafico_constructoras,
    grafico_distritos,
    grafico_estado,
    grafico_evolucion,
    grafico_mes,
    grafico_presupuesto,
)
from codigo.dashboard.kpis import calcular_kpis
from codigo.dashboard.mapas import grafico_mapa
from codigo.dashboard.utils import (
    obras_por_anio,
    obras_por_distrito,
    obras_por_estado,
    obras_por_mes,
    preparar_fechas,
    preparar_geodatos,
    preparar_tabla,
    presupuesto_por_distrito,
    top_constructoras,
)

st.set_page_config(
    page_title="Barcelona Open Data ETL",
    page_icon="🏗️",
    layout="wide",
)

# ===============================
# Cargar datos/ fichero datos.py
# ===============================

df = cargar_datos()

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

# PESTAÑAS
tab_resumen, tab_mapa, tab_datos, tab_estadisticas = st.tabs(
    [
        "📊 Resumen",
        "🗺️ Mapa",
        "📋 Datos",
        "📈 Estadísticas",
    ]
)

# ===============================

# ===============================
# Sidebar filtros
# ===============================

df = aplicar_filtros(df)


st.sidebar.divider()
# Número de registros filtrados
st.sidebar.metric(
    "Obras mostradas",
    len(df),
)
# Fecha Última actualización
st.sidebar.caption(f"Última actualización: {datetime.now():%d/%m/%Y %H:%M}")
# Información del proyecto en la barra lateral
st.sidebar.markdown("### ℹ️ Proyecto")

st.sidebar.info(
    """
**Barcelona Open Data ETL**

Dashboard construido con:

- Python
- Pandas
- SQLite
- Plotly
- Streamlit
"""
)


# ===============================
# KPIs
# ===============================

kpis = calcular_kpis(df)

# ===============================
# Datos para gráficos
# ===============================
# Para cálculos
df_graficos = df.copy()
df_graficos["fecha_inicio"] = pd.to_datetime(
    df_graficos["fecha_inicio"],
    errors="coerce",
)

df = preparar_fechas(df)

df_tabla = preparar_tabla(df)
df_tabla = df_tabla.drop(columns=["geometria_wgs84"])

gdf = preparar_geodatos(df)

obras_distrito = obras_por_distrito(df)

estado_df = obras_por_estado(df)

# obras_anio = obras_por_anio(df)
obras_anio = obras_por_anio(df_graficos)
constructoras = top_constructoras(df)

presupuesto_distrito = presupuesto_por_distrito(df)

# obras_mes, meses = obras_por_mes(df)
obras_mes, meses = obras_por_mes(df_graficos)

# ===============================
# ===============================
# Fin datos para gráficos
# ===============================
fig_distritos = grafico_distritos(obras_distrito)

fig_estado = grafico_estado(estado_df)

fig_evolucion = grafico_evolucion(obras_anio)

fig_constructoras = grafico_constructoras(constructoras)

fig_presupuesto = grafico_presupuesto(presupuesto_distrito)

fig_mes = grafico_mes(obras_mes, meses)
# ===============================
# Gráficos
# ===============================
# PESTAÑA RESUMEN
with tab_resumen:
    fila1 = st.columns(4)

    fila1[0].metric("🏗️ Obras", f"{kpis['total_obras']:,}")
    fila1[1].metric("🏙️ Distritos", kpis["total_distritos"])
    fila1[2].metric("💰 Presupuesto", f"{kpis['presupuesto_total']:,.0f} €")
    fila1[3].metric("📅 Duración media", f"{kpis['duracion_media']:.0f} días")

    fila2 = st.columns(4)

    fila2[0].metric("✅ Finalizadas", kpis["obras_finalizadas"])
    fila2[1].metric("🏢 Constructoras", kpis["total_constructoras"])
    fila2[2].metric("🚧 Tipos de obra", kpis["total_tipos"])
    fila2[3].metric("📍 Barrios", kpis["total_barrios"])
    st.divider()
    # Primera fila de gráficos
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
    # Gráfico evolución
    st.plotly_chart(
        fig_evolucion,
        width="stretch",
        key="grafico_evolucion",
    )
    col1, col2 = st.columns(2)
    # Gráfico POR MESES
    with col1:
        st.plotly_chart(
            fig_mes,
            width="stretch",
            key="grafico_mes",
        )
    # Gráfico PRESUPUESTOS
    with col2:
        st.plotly_chart(
            fig_presupuesto,
            width="stretch",
            key="grafico_presupuesto",
        )
    # Gráfico TOP 10 CONSTRUCTORAS
    st.plotly_chart(
        fig_constructoras,
        width="stretch",
        key="grafico_constructoras",
    )
# ===============================
# Mapa interactivo
# ===============================
with tab_mapa:
    st.subheader("Mapa de obras")

    fig_mapa = grafico_mapa(gdf)

    st.plotly_chart(
        fig_mapa,
        width="stretch",
        key="mapa_obras",
    )

# ===============================
# Descargar datos
# ===============================
# Tabla
csv = df_tabla.to_csv(index=False).encode("utf-8")
with tab_datos:
    st.download_button(
        label="📥 Descargar datos filtrados (CSV)",
        data=csv,
        file_name="obras_filtradas.csv",
        mime="text/csv",
    )
    st.subheader("Datos")

    st.dataframe(
        df_tabla,
        width="stretch",
    )
# ===============================
# Estadísticas generales

with tab_estadisticas:

    st.subheader("Estadísticas generales")

    estadisticas = df.describe(include="all").fillna("").astype(str)

    st.dataframe(estadisticas)
# ================================
st.divider()

st.caption(
    """
    Barcelona Open Data ETL • Dashboard interactivo desarrollado por Israel Mellado

    Datos: Ayuntamiento de Barcelona · Open Data BCN
    """
)
