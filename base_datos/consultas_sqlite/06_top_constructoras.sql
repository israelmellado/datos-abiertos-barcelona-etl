SELECT
    constructor,
    COUNT(*) AS obras
FROM obras
GROUP BY constructor
ORDER BY obras DESC
LIMIT 10;