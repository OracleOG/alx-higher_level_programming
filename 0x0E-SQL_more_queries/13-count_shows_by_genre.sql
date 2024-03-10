-- LIST genres in hbtn_0d_tvshows db
-- group the genres and display the number of shows linked to a genre
SELECT tv_genres.name, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_show_genres 
	LEFT JOIN tv_genres  ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;