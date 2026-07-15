import pandas as pd

from codigo.base_datos.conexion import obtener_conexion
from codigo.configuracion.config import CONSULTAS_BI, CONSULTAS_SQL

# =====================================
# Ruta de consultas según el motor
# =====================================

RUTA_CONSULTAS = CONSULTAS_SQL


def ejecutar_consulta(nombre_sql):
    """Ejecuta una consulta SQL y devuelve un DataFrame."""

    conexion = obtener_conexion()
    with open(RUTA_CONSULTAS / nombre_sql, encoding="utf-8") as archivo:
        consulta = archivo.read()

    df = pd.read_sql_query(consulta, conexion)

    conexion.close()

    return df


def mostrar_consultas():
    """Lista las consultas disponibles."""

    consultas = sorted(RUTA_CONSULTAS.glob("*.sql"))

    for i, consulta in enumerate(consultas, start=1):
        print(f"{i}. {consulta.stem}")

    return consultas


def ejecutar_consulta_bi(nombre_sql):
    """Ejecuta una consulta Business Intelligence."""

    conexion = obtener_conexion()

    with open(CONSULTAS_BI / nombre_sql, encoding="utf-8") as archivo:
        consulta = archivo.read()

    df = pd.read_sql_query(consulta, conexion)

    for columna in df.columns:
        if df[columna].dtype == "object":
            try:
                df[columna] = pd.to_numeric(df[columna])
            except Exception:
                pass

    conexion.close()

    return df


def main():

    print("=" * 60)
    print("CONSULTAS SQL")
    print("=" * 60)

    consultas = mostrar_consultas()

    opcion = int(input("\nSeleccione una consulta: "))

    resultado = ejecutar_consulta(
        consultas[opcion - 1].name,
    )

    print()
    print(resultado)


if __name__ == "__main__":
    main()
