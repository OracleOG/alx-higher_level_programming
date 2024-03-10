-- list all cities contained in the db
-- with their corresponding states
SELECT cities.id, cities.name, states.name
FROM  cities 
LEFT JOIN states ON cities.state_id = states.id