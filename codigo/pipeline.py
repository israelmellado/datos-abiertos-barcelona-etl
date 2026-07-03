from pathlib import Path
import subprocess
import sys

RAIZ_PROYECTO = Path(__file__).resolve().parents[1]
sys.path.append(str(RAIZ_PROYECTO))

from codigo.configuracion.config import PIPELINE_SCRIPTS
from codigo.utilidades.logger import logger

RAIZ = Path(__file__).resolve().parent


def main() -> None:
    print("=" * 60)
    print("PIPELINE ETL BARCELONA OPEN DATA")
    print("=" * 60)

    logger.info("Inicio del pipeline")

    for nombre, script in PIPELINE_SCRIPTS:

        print(f"\n▶ {nombre}")
        logger.info(nombre)

        ruta = RAIZ / script

        if not ruta.exists():
            print(f"\n❌ No existe: {ruta}")
            logger.error(f"No existe el script: {ruta}")
            sys.exit(1)

        print(f"\n▶ Ejecutando: {script}")
        logger.info(f"Ejecutando: {script}")

        resultado = subprocess.run(
            [sys.executable, str(ruta)],
            cwd=RAIZ,
            check=False,
        )

        if resultado.returncode != 0:
            print(f"\n❌ Error en: {script}")
            logger.error(f"Error ejecutando: {script}")
            sys.exit(resultado.returncode)

        print("✔ Finalizado")
        logger.info(f"Finalizado correctamente: {script}")

    print("\nPIPELINE FINALIZADO CORRECTAMENTE")
    logger.info("Pipeline finalizado correctamente")


if __name__ == "__main__":
    main()