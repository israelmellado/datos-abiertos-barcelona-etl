import streamlit as st


def aplicar_filtros(df):
    """Aplica los filtros del dashboard."""

    st.sidebar.header("Filtros")

    # Distrito
    distritos = sorted(df["distrito"].dropna().unique())

    distrito = st.sidebar.selectbox(
        "Distrito",
        ["Todos"] + distritos,
    )

    if distrito != "Todos":
        df = df[df["distrito"] == distrito]

    # Estado
    estados = sorted(df["estado"].dropna().unique())

    estado = st.sidebar.selectbox(
        "Estado",
        ["Todos"] + estados,
    )

    if estado != "Todos":
        df = df[df["estado"] == estado]

    # Tipo
    tipos = sorted(df["tipo_obra"].dropna().unique())

    tipo = st.sidebar.selectbox(
        "Tipo de obra",
        ["Todos"] + tipos,
    )

    if tipo != "Todos":
        df = df[df["tipo_obra"] == tipo]

    # Buscar
    st.sidebar.subheader("Buscar obra")

    texto = st.sidebar.text_input(
        "Nombre o descripción",
    )

    if texto:
        df = df[
            df["descripcion"].str.contains(
                texto,
                case=False,
                na=False,
            )
        ]

    return df
