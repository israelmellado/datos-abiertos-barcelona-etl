SELECT
    SUBSTR(fecha_inicio,1,7) AS mes,

    ROUND(
        SUM(presupuesto_adjudicacion)::numeric,
        2
    ) AS presupuesto_total
FROM obras
WHERE fecha_inicio IS NOT NULL
GROUP BY mes
ORDER BY mes;