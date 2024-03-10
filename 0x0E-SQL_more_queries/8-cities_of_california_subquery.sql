-- list records 
-- records from the hbtn_0d_usa table
SELECT cities.id, cities.name
FROM  cities
WHERE state_id =
(SELECT id
FROM states
WHERE name = 'California')