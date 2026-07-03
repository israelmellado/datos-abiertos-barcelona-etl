SELECT
    ROUND(AVG(presupuesto_licitacion),2) AS licitacion_media,
    ROUND(AVG(presupuesto_adjudicacion),2) AS adjudicacion_media
FROM obras;