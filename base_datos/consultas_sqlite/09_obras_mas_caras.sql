SELECT
    titulo,
    distrito,
    presupuesto_licitacion
FROM obras
ORDER BY presupuesto_licitacion DESC
LIMIT 10;