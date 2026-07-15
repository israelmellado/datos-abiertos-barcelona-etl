SELECT
    ROUND(CAST(AVG(presupuesto_licitacion) AS numeric), 2) AS licitacion_media,
    ROUND(CAST(AVG(presupuesto_adjudicacion) AS numeric), 2) AS adjudicacion_media
FROM obras;