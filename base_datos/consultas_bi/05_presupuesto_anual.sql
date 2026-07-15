SELECT
    SUBSTR(fecha_inicio,1,4) AS anio,

    ROUND(
        SUM(presupuesto_adjudicacion)::numeric,
        2
    ) AS presupuesto_total
FROM obras
WHERE fecha_inicio IS NOT NULL
GROUP BY anio
ORDER BY anio;