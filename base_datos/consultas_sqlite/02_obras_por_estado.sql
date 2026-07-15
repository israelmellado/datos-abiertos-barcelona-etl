SELECT
    estado,
    COUNT(*) AS numero_obras
FROM obras
GROUP BY estado
ORDER BY numero_obras DESC;