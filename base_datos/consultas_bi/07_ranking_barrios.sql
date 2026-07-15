SELECT
    barrio,

    ROUND(
        SUM(presupuesto_adjudicacion)::numeric,
        2
    ) AS inversion_total

FROM obras

GROUP BY barrio

ORDER BY inversion_total DESC

LIMIT 20;