def calcular_kpis(df):
    """Calcula los indicadores principales del dashboard."""

    return {
        "total_obras": len(df),
        "total_distritos": df["distrito"].nunique(),
        "presupuesto_total": df["presupuesto_licitacion"].sum(),
        "duracion_media": df["duracion_dias"].mean(),
        "obras_finalizadas": (df["estado"] == "Finalitzada").sum(),
        "total_constructoras": df["constructor"].nunique(),
        "total_tipos": df["tipo_obra"].nunique(),
        "total_barrios": df["barrio"].nunique(),
    }
