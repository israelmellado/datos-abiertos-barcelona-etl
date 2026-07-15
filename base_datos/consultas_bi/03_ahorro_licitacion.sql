SELECT
    ROUND(
        SUM(
             presupuesto_licitacion -
             presupuesto_adjudicacion
        )::numeric,
        2
    ) AS ahorro_total,

    ROUND(
        AVG(
            presupuesto_licitacion -
            presupuesto_adjudicacion
        )::numeric,
        2
    ) AS ahorro_medio
FROM obras;