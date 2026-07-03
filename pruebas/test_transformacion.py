import pandas as pd

from codigo.configuracion.config import CSV_LIMPIO


def test_csv_limpio_existe():
    assert CSV_LIMPIO.exists()


def test_csv_no_esta_vacio():
    df = pd.read_csv(CSV_LIMPIO)
    assert len(df) > 0


def test_no_hay_codigos_duplicados():
    df = pd.read_csv(CSV_LIMPIO)
    assert not df["codi"].duplicated().any()


def test_existe_columna_duracion():
    df = pd.read_csv(CSV_LIMPIO)
    assert "duracion_dias" in df.columns


def test_duracion_tiene_valores():
    df = pd.read_csv(CSV_LIMPIO)
    assert df["duracion_dias"].notna().sum() > 0


def test_columnas_esperadas():
    df = pd.read_csv(CSV_LIMPIO)

    columnas = {
        "codi",
        "ubicacio",
        "nom_districte",
        "nom_barri",
        "tipusobra",
        "pressupost_licitacio",
        "pressupost_adjudicacio",
        "data_inici",
        "data_fi",
        "duracion_dias",
        "promotor",
        "constructor",
        "estat",
        "titol",
        "descripcio",
        "url_web_obres",
        "geometria_wgs84",
    }

    assert columnas.issubset(df.columns)