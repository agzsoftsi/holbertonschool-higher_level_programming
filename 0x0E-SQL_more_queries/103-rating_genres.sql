-- List all genres by their rating
-- display: tv_shows.title - rating sum, sorted in descending order by the rating
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating FROM tv_show_ratings JOIN tv_shows ON tv_shows.id = tv_show_ratings.show_id JOIN tv_show_genres ON tv_show_genres.show_id = tv_show_ratings.show_id JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.name ORDER BY rating DESC;
