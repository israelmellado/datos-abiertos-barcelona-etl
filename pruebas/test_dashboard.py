from codigo.configuracion.config import IMAGENES


def test_directorio_imagenes_existe():
    assert IMAGENES.exists()


def test_se_han_generado_graficos():

    imagenes = [
        "01_obras_por_distrito.png",
        "02_estado_obras.png",
        "03_duracion_obras.png",
        "04_tipos_obra.png",
    ]

    for imagen in imagenes:
        assert (IMAGENES / imagen).exists()


def test_los_graficos_no_estan_vacios():

    imagenes = IMAGENES.glob("*.png")

    for imagen in imagenes:
        assert imagen.stat().st_size > 0