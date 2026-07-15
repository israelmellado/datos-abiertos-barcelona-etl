SELECT
    tipo_obra,
    COUNT(*) AS total
FROM obras
GROUP BY tipo_obra
ORDER BY total DESC;