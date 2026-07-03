import sys
from pathlib import Path

RAIZ_PROYECTO = Path(__file__).resolve().parents[1]
sys.path.append(str(RAIZ_PROYECTO))

from codigo.configuracion.config import (
    BASE_DATOS,
    CSV_CRUDO,
    CSV_LIMPIO,
    IMAGENES,
    LOGS,
    MODELO_SQL,
)


def test_rutas_configuracion():

    assert isinstance(CSV_CRUDO, Path)
    assert isinstance(CSV_LIMPIO, Path)
    assert isinstance(BASE_DATOS, Path)
    assert isinstance(MODELO_SQL, Path)
    assert isinstance(IMAGENES, Path)
    assert isinstance(LOGS, Path)


def test_archivos_principales_existen():

    assert MODELO_SQL.exists()
    assert CSV_CRUDO.exists()
    assert CSV_LIMPIO.exists()


def test_directorios_existen():

    assert IMAGENES.exists()
    assert LOGS.exists()
