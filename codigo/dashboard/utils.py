import geopandas as gpd
import pandas as pd
from shapely import wkt


# ===============================
# Geometría para el mapa
# ===============================
# Preparar el GeoDataFrame
def preparar_geodatos(df):
    """Convierte la geometría WKT en un GeoDataFrame."""

    gdf = gpd.GeoDataFrame(
        df.copy(),
        geometry=df["geometria_wgs84"].apply(wkt.loads),
        crs="EPSG:4326",
    )
    # Calcular centroides de forma correcta
    gdf_utm = gdf.to_crs(epsg=25831)

    gdf["lon"] = gdf_utm.centroid.to_crs(epsg=4326).x
    gdf["lat"] = gdf_utm.centroid.to_crs(epsg=4326).y

    return gdf


# Preparar fechas
def preparar_fechas(df):
    """Convierte fecha_inicio a datetime."""

    df = df.copy()

    df["fecha_inicio"] = pd.to_datetime(
        df["fecha_inicio"],
        errors="coerce",
    )

    return df


def preparar_tabla(df):
    """Convierte la fecha de inicio a datetime."""

    tabla = df.copy()

    if "fecha_inicio" in tabla.columns:
        tabla["fecha_inicio"] = (
            pd.to_datetime(
                tabla["fecha_inicio"],
                errors="coerce",
            )
            .dt.strftime("%Y-%m-%d")
            .fillna("")
            .astype(str)
        )
    # Convertir TODAS las columnas object a string
    for col in tabla.select_dtypes(include="object").columns:
        tabla[col] = tabla[col].fillna("").astype(str)

    return tabla


# Obras por distrito
def obras_por_distrito(df):

    return (
        df.groupby("distrito")
        .size()
        .reset_index(name="obras")
        .sort_values("obras", ascending=False)
    )


# Obras por estado
def obras_por_estado(df):

    return df.groupby("estado").size().reset_index(name="obras")


# Evolución anual
def obras_por_anio(df):

    return (
        df.dropna(subset=["fecha_inicio"])
        .assign(anio=lambda x: x["fecha_inicio"].dt.year)
        .groupby("anio")
        .size()
        .reset_index(name="obras")
        .sort_values("anio")
    )


# Constructoras
def top_constructoras(df):

    return (
        df.groupby("constructor")
        .size()
        .reset_index(name="obras")
        .sort_values("obras", ascending=False)
        .head(10)
    )


# Presupuesto
def presupuesto_por_distrito(df):

    return (
        df.groupby("distrito")["presupuesto_licitacion"]
        .sum()
        .reset_index()
        .sort_values(
            "presupuesto_licitacion",
            ascending=False,
        )
    )


# Obras por mes


def obras_por_mes(df):

    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
    }

    datos = (
        df.dropna(subset=["fecha_inicio"])
        .assign(mes=lambda x: x["fecha_inicio"].dt.month)
        .groupby("mes")
        .size()
        .reindex(range(1, 13), fill_value=0)
        .reset_index(name="obras")
    )

    datos["mes"] = datos["mes"].map(meses)

    return datos, meses
