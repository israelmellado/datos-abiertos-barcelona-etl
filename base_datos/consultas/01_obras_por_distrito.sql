SELECT
    distrito,
    COUNT(*) AS numero_obras
FROM obras
GROUP BY distrito
ORDER BY numero_obras DESC;