-- List all genres in hbtn_0d_tvshows with the number of shows linked to each
-- display: <TV Show genre> - <Number of shows linked to this genre>, First column must be called genre, Don’t display a genre that doesn’t have any shows linked,sorted in desc shows
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows FROM tv_show_genres LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id GROUP BY genre ORDER BY number_of_shows DESC;
