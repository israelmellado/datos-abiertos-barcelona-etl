import pandas as pd

from codigo.configuracion.config import CSV_CRUDO


def test_csv_crudo_existe():
    assert CSV_CRUDO.exists()


def test_csv_crudo_no_esta_vacio():

    df = pd.read_csv(CSV_CRUDO)

    assert len(df) > 0


def test_csv_crudo_tiene_columnas():

    df = pd.read_csv(CSV_CRUDO)

    columnas = {
        "codi",
        "nom_districte",
        "nom_barri",
        "tipusobra",
        "data_inici",
        "data_fi",
    }

    assert columnas.issubset(df.columns)