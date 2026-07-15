# from codigo.configuracion.config import MOTOR_BD

# if MOTOR_BD == "sqlite":
#    pass

# elif MOTOR_BD == "postgres":
#    pass

# else:
#    raise ValueError(f"Motor no soportado: {MOTOR_BD}")
from codigo.base_datos.postgres import obtener_conexion_postgres
from codigo.base_datos.sqlite import obtener_conexion_sqlite
from codigo.configuracion.config import MOTOR_BD


def obtener_conexion():
    """Devuelve una conexión según el motor configurado."""

    if MOTOR_BD == "sqlite":
        return obtener_conexion_sqlite()

    if MOTOR_BD == "postgres":
        return obtener_conexion_postgres()

    raise ValueError(f"Motor no soportado: {MOTOR_BD}")
