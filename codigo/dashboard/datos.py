import sqlite3

import pandas as pd

from codigo.configuracion.config import BASE_DATOS


def cargar_datos():
    """Carga la tabla de obras desde SQLite."""

    conexion = sqlite3.connect(BASE_DATOS)

    df = pd.read_sql(
        "SELECT * FROM obras",
        conexion,
    )

    conexion.close()

    return df
