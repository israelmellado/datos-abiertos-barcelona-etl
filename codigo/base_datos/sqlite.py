import sqlite3

from codigo.configuracion.config import BASE_DATOS


def obtener_conexion_sqlite():
    """Devuelve una conexión SQLite."""
    return sqlite3.connect(BASE_DATOS)
