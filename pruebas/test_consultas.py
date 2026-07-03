from pathlib import Path
import sqlite3

import pandas as pd

from codigo.configuracion.config import BASE_DATOS, CONSULTAS_SQL


def test_directorio_consultas_existe():
    assert CONSULTAS_SQL.exists()
    assert CONSULTAS_SQL.is_dir()


def test_hay_consultas_sql():
    consultas = list(CONSULTAS_SQL.glob("*.sql"))
    assert len(consultas) > 0


def test_todas_las_consultas_se_ejecutan():

    conexion = sqlite3.connect(BASE_DATOS)

    for archivo_sql in CONSULTAS_SQL.glob("*.sql"):

        with open(archivo_sql, encoding="utf-8") as f:
            consulta = f.read()

        resultado = pd.read_sql_query(consulta, conexion)

        assert isinstance(resultado, pd.DataFrame)
        assert len(resultado) > 0

    conexion.close()