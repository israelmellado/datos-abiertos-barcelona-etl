import sqlite3

from codigo.configuracion.config import BASE_DATOS


def test_base_datos_existe():
    assert BASE_DATOS.exists()


def test_tabla_obras_existe():
    conexion = sqlite3.connect(BASE_DATOS)

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name='obras'
    """)

    resultado = cursor.fetchone()

    conexion.close()

    assert resultado is not None


def test_tabla_obras_tiene_registros():
    conexion = sqlite3.connect(BASE_DATOS)

    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM obras")

    total = cursor.fetchone()[0]

    conexion.close()

    assert total > 0


def test_codigo_es_unico():
    conexion = sqlite3.connect(BASE_DATOS)

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT COUNT(codigo),
               COUNT(DISTINCT codigo)
        FROM obras
    """)

    total, distintos = cursor.fetchone()

    conexion.close()

    assert total == distintos