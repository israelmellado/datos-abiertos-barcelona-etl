SELECT
    codigo,
    titulo,
    distrito,
    constructor,
    duracion_dias
FROM obras
ORDER BY duracion_dias DESC
LIMIT 20;