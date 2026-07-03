from pathlib import Path
import subprocess
import sys

RAIZ_PROYECTO = Path(__file__).resolve().parents[1]
sys.path.append(str(RAIZ_PROYECTO))

from codigo.utilidades.logger import logger
from codigo.configuracion.config import PIPELINE_SCRIPTS

RAIZ = Path(__file__).resolve().parent



print("=" * 60)
print("PIPELINE ETL BARCELONA OPEN DATA")
print("=" * 60)

logger.info("Inicio del pipeline")
pipeline_ok = True

for nombre, script in PIPELINE_SCRIPTS:

    print(f"\n▶ {nombre}")
    logger.info(nombre)

    ruta = RAIZ / script

    if not ruta.exists():
        print(f"❌ No existe: {ruta}")
        logger.error(f"No existe el script: {ruta}")
        pipeline_ok = False
        break

    print(f"\n▶ Ejecutando: {script}")
    logger.info(f"Ejecutando: {script}")

    resultado = subprocess.run([sys.executable, str(ruta)])
    
    if resultado.returncode == 0:
        logger.info(f"Finalizado correctamente: {script}")
        print("✔ Finalizado")

    if resultado.returncode != 0:
        print(f"\n❌ Error en: {script}")
        logger.error(f"Error ejecutando: {script}")
        pipeline_ok = False
        break

if pipeline_ok:
    print("PIPELINE FINALIZADO CORRECTAMENTE")
    logger.info("Pipeline finalizado correctamente")
else:
    print("PIPELINE FINALIZADO CON ERRORES")
    logger.error("Pipeline finalizado con errores")
