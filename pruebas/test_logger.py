from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parents[2]
sys.path.append(str(RAIZ))

from codigo.utilidades.logger import logger

logger.info("Inicio del pipeline")
logger.warning("Esto es una advertencia")
logger.error("Esto es un error de prueba")