import plotly.express as px


def grafico_distritos(obras_distrito):
    fig = px.bar(
        obras_distrito,
        x="distrito",
        y="obras",
        title="Número de obras por distrito",
    )

    return fig


def grafico_estado(estado_df):
    fig = px.pie(
        estado_df,
        names="estado",
        values="obras",
        title="Distribución de las obras por estado",
    )

    return fig


def grafico_evolucion(obras_anio):

    fig = px.line(
        obras_anio,
        x="anio",
        y="obras",
        markers=True,
        title="Evolución de las obras por año",
    )

    fig.update_layout(
        xaxis_title="Año",
        yaxis_title="Número de obras",
    )

    return fig


def grafico_constructoras(constructoras):

    fig = px.bar(
        constructoras,
        x="obras",
        y="constructor",
        orientation="h",
        title="Top 10 constructoras",
    )

    fig.update_layout(yaxis=dict(categoryorder="total ascending"))

    return fig


def grafico_presupuesto(presupuesto_distrito):

    fig = px.bar(
        presupuesto_distrito,
        x="distrito",
        y="presupuesto_licitacion",
        title="Presupuesto por distrito",
        text_auto=".2s",
    )

    fig.update_layout(
        xaxis_title="Distrito",
        yaxis_title="Presupuesto (€)",
    )

    return fig


def grafico_mes(obras_mes, meses):

    fig = px.bar(
        obras_mes,
        x="mes",
        y="obras",
        title="Inicio de obras por mes",
        text_auto=True,
    )

    fig.update_xaxes(
        categoryorder="array",
        categoryarray=list(meses.values()),
    )

    return fig
