SELECT
    strftime('%Y', fecha_inicio) AS anio,
    COUNT(*) AS obras
FROM obras
WHERE fecha_inicio IS NOT NULL
GROUP BY anio
ORDER BY anio;