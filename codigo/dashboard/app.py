import sys
from datetime import datetime
from pathlib import Path

import pandas as pd
import streamlit as st

RAIZ_PROYECTO = Path(__file__).resolve().parents[2]
sys.path.append(str(RAIZ_PROYECTO))

from codigo.configuracion.config import CONSULTAS_BI, CONSULTAS_SQL

RUTA_SQL = CONSULTAS_SQL
RUTA_BI = CONSULTAS_BI

from codigo.configuracion.config import IMAGENES

BANNER = IMAGENES / "banner.png"
from codigo.configuracion.config import BASE_DATOS
from codigo.dashboard.tema import aplicar_tema
from codigo.dashboard.visualizaciones_bi import mostrar_visualizaciones

ultima = datetime.fromtimestamp(Path(BASE_DATOS).stat().st_mtime)

from codigo.analisis.consultas import (
    ejecutar_consulta,
    ejecutar_consulta_bi,
)
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
from codigo.dashboard.graficos_bi import (
    grafico_obras_largas,
)
from codigo.dashboard.kpis import calcular_kpis
from codigo.dashboard.kpis_bi import calcular_kpis_bi
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

CONSULTAS = {
    "Obras por distrito": "01_obras_por_distrito.sql",
    "Obras por estado": "02_obras_por_estado.sql",
    "Duración media": "03_duracion_media.sql",
    "Tipos de obra": "04_top_tipos_obra.sql",
    "Presupuesto medio": "05_presupuesto_medio.sql",
    "Top constructoras": "06_top_constructoras.sql",
}

# Selector consultas BI
CONSULTAS_BI_MENU = {
    "Inversión por distrito": "01_inversion_por_distrito.sql",
    "Constructoras por inversión": "02_constructoras_inversion.sql",
    "Ahorro licitación": "03_ahorro_licitacion.sql",
    "Obras más largas": "04_obras_mas_largas.sql",
    "Presupuesto anual": "05_presupuesto_anual.sql",
    "Presupuesto mensual": "06_presupuesto_mensual.sql",
    "Ranking barrios": "07_ranking_barrios.sql",
    "Presupuesto por estado": "08_presupuesto_por_estado.sql",
    "Distribución presupuestos": "09_distribucion_presupuesto.sql",
    "Duración vs presupuesto": "10_duracion_vs_presupuesto.sql",
}

st.set_page_config(
    layout="wide",
)
aplicar_tema()
# ===============================
# Cargar datos/ fichero datos.py
# ===============================

df = cargar_datos()
total_obras = len(df)
# ===============================
# Título
# ===============================
st.title("🏗️ Barcelona Open Data ETL")
st.image(
    BANNER,
    width="stretch",
)
st.markdown(
    """
Dashboard interactivo construido a partir del pipeline ETL del proyecto.

Permite explorar las obras públicas del Ayuntamiento de Barcelona.
"""
)

st.divider()

# PESTAÑAS
tab_resumen, tab_mapa, tab_datos, tab_estadisticas, tab_sql, tab_bi = st.tabs(
    [
        "📊 Resumen",
        "🗺️ Mapa",
        "📋 Datos",
        "📈 Estadísticas",
        "🗄️ SQL",
        "🧠 Business Intelligence",
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
# Fecha Última actualización de la base de datos
st.sidebar.write("Última actualización de CONSULTAS SQL")
st.sidebar.caption(f"Última actualización: {ultima:%d/%m/%Y %H:%M}")
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

# DataFrame para cálculos con fechas
df_graficos = preparar_fechas(df.copy())

# DataFrame para la tabla
df_tabla = preparar_tabla(df)
df_tabla = df_tabla.drop(columns=["geometria_wgs84"])

# GeoDataFrame
gdf = preparar_geodatos(df)

# Agrupaciones sin fechas
obras_distrito = obras_por_distrito(df)
estado_df = obras_por_estado(df)
constructoras = top_constructoras(df)
presupuesto_distrito = presupuesto_por_distrito(df)

# Agrupaciones que necesitan datetime
obras_anio = obras_por_anio(df_graficos)
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
    st.info(f"Mostrando {len(df)} obras " f"de {kpis['total_obras']} disponibles.")
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
    st.write("DATOS")
    col1, col2 = st.columns([3, 1])
    with col1:
        if len(df_tabla) == kpis["total_obras"]:
            st.caption(f"Total de obras: {len(df_tabla):,}")
        else:
            st.caption(f"Mostrando {len(df_tabla):,} de {kpis['total_obras']:,} obras.")

    with col2:

        st.download_button(
            label="📥 Descargar datos filtrados (CSV)",
            data=csv,
            file_name="obras_filtradas.csv",
            mime="text/csv",
        )
    st.subheader("Datos")

    columnas = [
        "codigo",
        "titulo",
        "distrito",
        "barrio",
        "estado",
        "constructor",
        "fecha_inicio",
        "duracion_dias",
        "presupuesto_licitacion",
    ]

    vista = df_tabla[columnas].copy()

    st.dataframe(
        vista,
        width="stretch",
    )


# ===============================
# Estadísticas generales

with tab_estadisticas:
    st.subheader("📈 Estadísticas numéricas")

    estadisticas = df.select_dtypes(include="number").describe().T.round(2)

    st.dataframe(
        estadisticas,
        width="stretch",
    )
    st.subheader("📋 Información del conjunto de datos")

    tipos = (
        df.dtypes.astype(str)
        .rename("Tipo")
        .reset_index()
        .rename(columns={"index": "Columna"})
    )

    st.dataframe(
        tipos,
        width="stretch",
    )
# ================================
# Apartado consultas

with tab_sql:

    st.subheader("Consultas SQL")

    opcion = st.selectbox(
        "Seleccione una consulta",
        list(CONSULTAS.keys()),
    )

    resultado = ejecutar_consulta(CONSULTAS[opcion])

    st.dataframe(
        resultado,
        width="stretch",
    )

    sql = (RUTA_SQL / CONSULTAS[opcion]).read_text(encoding="utf-8")

    st.code(sql, language="sql")
    # "Obras por distrito"
    if opcion == "Obras por distrito":
        fig = grafico_distritos(resultado.rename(columns={"numero_obras": "obras"}))
        st.plotly_chart(fig, width="stretch")
    # "Obras por estado"
    elif opcion == "Obras más largas":

        fig = grafico_obras_largas(resultado)

        st.plotly_chart(
            fig,
            width="stretch",
        )
    # "Top constructoras"
    elif opcion == "Top constructoras":

        fig = grafico_constructoras(resultado)

        st.plotly_chart(fig, width="stretch")
    # "Presupuesto medio"
    elif opcion == "Presupuesto medio":

        st.metric(
            "Licitación media",
            f"{resultado.iloc[0]['licitacion_media']:,.2f} €",
        )

        st.metric(
            "Adjudicación media",
            f"{resultado.iloc[0]['adjudicacion_media']:,.2f} €",
        )
    # "Top tipos de obra"
    elif opcion == "Top tipos de obra":

        st.bar_chart(resultado.set_index("tipo_obra"))
    # Descargar datos SQL
    csv = resultado.to_csv(index=False).encode("utf-8")
    st.download_button(
        "📥 Descargar resultado",
        csv,
        "consulta.csv",
        "text/csv",
    )

# ================================

# Estadísticas generales
with tab_bi:

    st.header("Business Intelligence")
    kpis = calcular_kpis_bi(df)

    c1, c2, c3, c4, c5, c6 = st.columns(6)

    c1.metric("💰 Inversión", f"{kpis['inversion_total']:,.0f} €")

    c2.metric("🏗 Obras", f"{kpis['numero_obras']}")

    c3.metric("📍 Distritos", f"{kpis['numero_distritos']}")

    c4.metric("🏢 Constructoras", f"{kpis['numero_constructoras']}")

    c5.metric("📅 Duración", f"{kpis['duracion_media']:.0f} días")

    c6.metric("✅ Finalizadas", f"{kpis['porcentaje_finalizadas']:.1f}%")
    st.info(
        """
        Consultas analíticas realizadas directamente sobre la base de datos.

        Permiten obtener indicadores de negocio e información estratégica
        sobre las obras públicas de Barcelona.
        """
    )

    # Seleccionar consulta
    opcion_bi = st.selectbox(
        "Consulta BI",
        list(CONSULTAS_BI_MENU.keys()),
    )

    # Ejecutar consultas
    resultado = ejecutar_consulta_bi(CONSULTAS_BI_MENU[opcion_bi])

    sql = (CONSULTAS_BI / CONSULTAS_BI_MENU[opcion_bi]).read_text(encoding="utf-8")

    # Mostrar resultado
    st.code(sql, language="sql")

    st.dataframe(
        resultado,
        width="stretch",
    )
    mostrar_visualizaciones(
        opcion_bi,
        resultado,
    )
    csv = resultado.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Descargar CSV",
        csv,
        file_name=f"{CONSULTAS_BI_MENU[opcion_bi].replace('.sql','.csv')}",
        mime="text/csv",
    )
# ===============================
st.divider()

st.caption(
    """
    Barcelona Open Data ETL • Dashboard interactivo desarrollado por Israel Mellado

    Datos: Ayuntamiento de Barcelona · Open Data BCN
    """
)
