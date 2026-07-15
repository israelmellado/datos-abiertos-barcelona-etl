SELECT
    duracion_dias,
    presupuesto_adjudicacion,
    distrito
FROM obras
WHERE presupuesto_adjudicacion IS NOT NULL
AND duracion_dias IS NOT NULL;