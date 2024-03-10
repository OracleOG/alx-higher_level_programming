-- list all genres
-- only genres of the show 'Dexter'
SELECT tv_genres.name
FROM tv_show_genres 
	LEFT JOIN tv_shows  ON tv_show_genres.show_id = tv_shows.id
    LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE title = 'Dexter'
ORDER BY name ASC;