# import sqlite3
import pandas as pd

from codigo.base_datos.conexion import obtener_conexion


def cargar_datos():
    """Carga la tabla de obras desde SQLite."""

    # conexion = sqlite3.connect(BASE_DATOS)
    conexion = obtener_conexion()
    df = pd.read_sql(
        "SELECT * FROM obras",
        conexion,
    )

    conexion.close()

    return df
