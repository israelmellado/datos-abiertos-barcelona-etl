SELECT
    ROUND(AVG(presupuesto_licitacion)::numeric, 2) AS licitacion_media,
    ROUND(AVG(presupuesto_adjudicacion)::numeric, 2) AS adjudicacion_media
FROM obras;