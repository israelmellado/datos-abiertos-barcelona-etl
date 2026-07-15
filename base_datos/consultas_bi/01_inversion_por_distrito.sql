SELECT
    distrito,
    SUM(presupuesto_adjudicacion) AS inversion_total
FROM obras
GROUP BY distrito
ORDER BY inversion_total DESC;