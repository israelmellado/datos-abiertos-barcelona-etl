SELECT
    barrio,
    COUNT(*) AS obras
FROM obras
GROUP BY barrio
ORDER BY obras DESC
LIMIT 10;