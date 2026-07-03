from pathlib import Path
import logging

# ==========================
# Rutas
# ==========================

RAIZ = Path(__file__).resolve().parents[2]

CARPETA_LOGS = RAIZ / "logs"
CARPETA_LOGS.mkdir(exist_ok=True)

ARCHIVO_LOG = CARPETA_LOGS / "pipeline.log"

# ==========================
# Logger
# ==========================

logger = logging.getLogger("barcelona_etl")

if not logger.handlers:

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(ARCHIVO_LOG, encoding="utf-8")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)