import pandas as pd


def calcular_kpis_bi(df: pd.DataFrame):
    """Calcula los indicadores principales del dashboard BI."""

    inversion_total = df["presupuesto_adjudicacion"].sum()

    numero_obras = len(df)

    numero_distritos = df["distrito"].nunique()

    numero_constructoras = df["constructor"].dropna().nunique()

    duracion_media = df["duracion_dias"].mean()

    porcentaje_finalizadas = (df["estado"] == "Finalizada").mean() * 100

    return {
        "inversion_total": inversion_total,
        "numero_obras": numero_obras,
        "numero_distritos": numero_distritos,
        "numero_constructoras": numero_constructoras,
        "duracion_media": duracion_media,
        "porcentaje_finalizadas": porcentaje_finalizadas,
    }
