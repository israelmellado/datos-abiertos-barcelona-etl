from sqlalchemy import create_engine

from codigo.configuracion.config import (
    BASE_DATOS_POSTGRES,
    HOST,
    PASSWORD,
    PUERTO,
    USUARIO,
)

engine = create_engine(
    f"postgresql+psycopg2://"
    f"{USUARIO}:{PASSWORD}@"
    f"{HOST}:{PUERTO}/"
    f"{BASE_DATOS_POSTGRES}"
)


def obtener_conexion_postgres():
    return engine.connect()
