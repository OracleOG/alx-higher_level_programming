-- list records in table
-- exclude records with 'score' value empty
SELECT score, name
FROM second_table
WHERE score IS NOT NULL
ORDER BY score DESC;