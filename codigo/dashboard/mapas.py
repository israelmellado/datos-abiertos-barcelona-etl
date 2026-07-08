import plotly.express as px


def grafico_mapa(gdf):
    """Genera el mapa interactivo de las obras."""

    fig = px.scatter_map(
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

    return fig
