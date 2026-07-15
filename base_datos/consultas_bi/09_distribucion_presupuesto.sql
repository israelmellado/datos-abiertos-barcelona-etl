SELECT
    CASE
        WHEN presupuesto_adjudicacion < 100000 THEN '<100k'
        WHEN presupuesto_adjudicacion < 500000 THEN '100k-500k'
        WHEN presupuesto_adjudicacion < 1000000 THEN '500k-1M'
        WHEN presupuesto_adjudicacion < 5000000 THEN '1M-5M'
        ELSE '>5M'
    END AS rango,

    COUNT(*) AS numero_obras

FROM obras

GROUP BY rango

ORDER BY numero_obras DESC;