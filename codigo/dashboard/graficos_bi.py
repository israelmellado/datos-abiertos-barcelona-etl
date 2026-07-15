import plotly.express as px


def grafico_inversion_distrito(df):

    return px.bar(
        df,
        x="distrito",
        y="inversion_total",
        color="inversion_total",
    )


def grafico_constructoras_bi(df):
    df = df.copy()
    df["inversion_total"] = df["inversion_total"].astype(float)
    return px.bar(
        df,
        x="constructor",
        y="inversion_total",
        title="Constructoras por inversión",
    )


def grafico_presupuesto_anual(df):

    return px.line(
        df,
        x="anio",
        y="presupuesto_total",
        markers=True,
        title="Presupuesto anual",
    )


def grafico_presupuesto_mensual(df):

    return px.line(
        df,
        x="mes",
        y="presupuesto_total",
        markers=True,
        title="Presupuesto mensual",
    )


def grafico_barrios(df):

    return px.bar(
        df,
        x="inversion_total",
        y="barrio",
        orientation="h",
        title="Ranking de barrios",
    )


def grafico_presupuesto_estado(df):

    return px.pie(
        df,
        names="estado",
        values="presupuesto",
        title="Presupuesto por estado",
    )


def grafico_distribucion(df):

    return px.histogram(
        df,
        x="rango",
        y="numero_obras",
        title="Distribución de presupuestos",
    )


def grafico_dispersion(df):

    return px.scatter(
        df,
        x="duracion_dias",
        y="presupuesto_adjudicacion",
        color="distrito",
        title="Duración vs Presupuesto",
    )


def grafico_obras_largas(df):

    return px.bar(
        df,
        x="duracion_dias",
        y="titulo",
        orientation="h",
        color="duracion_dias",
        hover_data=[
            "distrito",
            "constructor",
        ],
        title="Obras con mayor duración",
    ).update_layout(yaxis={"categoryorder": "total ascending"})
