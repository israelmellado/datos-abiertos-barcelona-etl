SELECT
    constructor,
    COUNT(*) AS obras,
    ROUND(AVG(presupuesto_licitacion),2) AS presupuesto_medio
FROM obras
GROUP BY constructor
HAVING obras >= 3
ORDER BY presupuesto_medio DESC;