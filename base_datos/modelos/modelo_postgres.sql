DROP TABLE IF EXISTS obras;

CREATE TABLE obras (

    id SERIAL PRIMARY KEY,

    codigo VARCHAR(50) UNIQUE NOT NULL,

    ubicacion TEXT,

    distrito TEXT,

    barrio TEXT,

    tipo_obra TEXT,

    presupuesto_licitacion DOUBLE PRECISION,

    presupuesto_adjudicacion DOUBLE PRECISION,

    fecha_inicio DATE,

    fecha_fin DATE,

    duracion_dias INTEGER,

    promotor TEXT,

    constructor TEXT,

    estado TEXT,

    titulo TEXT,

    descripcion TEXT,

    url_web_obras TEXT,

    geometria_wgs84 TEXT

);