from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parents[2]

CSV = RAIZ / "datos" / "procesados" / "obres_limpias.csv"

df = pd.read_csv(CSV)

duplicados = df[df.duplicated(subset="codi", keep=False)]

print("Número de registros duplicados:", len(duplicados))
print()

print(duplicados[["codi", "titol", "data_inici", "data_fi"]].sort_values("codi").head(30))