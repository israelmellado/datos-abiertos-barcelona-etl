import streamlit as st

from codigo.dashboard.graficos_bi import (
    grafico_barrios,
    grafico_constructoras_bi,
    grafico_dispersion,
    grafico_distribucion,
    grafico_inversion_distrito,
    grafico_obras_largas,
    grafico_presupuesto_anual,
    grafico_presupuesto_estado,
    grafico_presupuesto_mensual,
)


def mostrar_visualizaciones(nombre, resultado):
    """Muestra automáticamente la visualización adecuada."""
    if nombre == "Inversión por distrito":

        fig = grafico_inversion_distrito(resultado)

        st.plotly_chart(fig, width="stretch")
    elif nombre == "Constructoras por inversión":

        fig = grafico_constructoras_bi(resultado)

        st.plotly_chart(fig, width="stretch")

    elif nombre == "Ahorro licitación":

        c1, c2 = st.columns(2)

        c1.metric(
            "Ahorro total",
            f"{resultado.iloc[0]['ahorro_total']:,.2f} €",
        )

        c2.metric(
            "Ahorro medio",
            f"{resultado.iloc[0]['ahorro_medio']:,.2f} €",
        )
    elif nombre == "Obras más largas":

        fig = grafico_obras_largas(resultado)

        st.plotly_chart(
            fig,
            width="stretch",
        )

    elif nombre == "Presupuesto mensual":

        fig = grafico_presupuesto_mensual(resultado)

        st.plotly_chart(fig, width="stretch")
    elif nombre == "Presupuesto anual":

        fig = grafico_presupuesto_anual(resultado)

        st.plotly_chart(fig, width="stretch")

    elif nombre == "Ranking barrios":

        fig = grafico_barrios(resultado)

        st.plotly_chart(fig, width="stretch")

    elif nombre == "Presupuesto por estado":

        fig = grafico_presupuesto_estado(resultado)

        st.plotly_chart(fig, width="stretch")

    elif nombre == "Distribución presupuestos":

        fig = grafico_distribucion(resultado)

        st.plotly_chart(fig, width="stretch")

    elif nombre == "Duración vs presupuesto":

        fig = grafico_dispersion(resultado)

        st.plotly_chart(fig, width="stretch")

    else:

        st.dataframe(resultado, width="stretch")
