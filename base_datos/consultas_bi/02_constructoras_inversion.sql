SELECT
    TRIM(constructor) AS constructor,

    ROUND(
        SUM(presupuesto_adjudicacion)::numeric,
        2
    ) AS inversion_total

FROM obras

WHERE
    constructor IS NOT NULL
    AND TRIM(constructor) <> '' AND presupuesto_adjudicacion IS NOT NULL

GROUP BY TRIM(constructor)

ORDER BY inversion_total DESC

LIMIT 20;