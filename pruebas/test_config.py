from pathlib import Path
import sys

RAIZ_PROYECTO = Path(__file__).resolve().parents[1]
sys.path.append(str(RAIZ_PROYECTO))

from codigo.configuracion.config import (
    CSV_CRUDO,
    CSV_LIMPIO,
    BASE_DATOS,
    MODELO_SQL,
    IMAGENES,
    LOGS,
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