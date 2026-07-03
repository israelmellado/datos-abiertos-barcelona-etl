DROP TABLE IF EXISTS obras;

CREATE TABLE obras (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    codigo TEXT NOT NULL UNIQUE,

    ubicacion TEXT,

    distrito TEXT,

    barrio TEXT,

    tipo_obra TEXT,

    presupuesto_licitacion REAL,

    presupuesto_adjudicacion REAL,

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