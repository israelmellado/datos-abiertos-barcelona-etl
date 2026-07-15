SELECT
    estado,
    ROUND(
        SUM(presupuesto_adjudicacion)::numeric,
        2
    ) AS presupuesto
FROM obras
GROUP BY estado
ORDER BY presupuesto DESC;