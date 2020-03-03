-- List all shows by their rating
-- display: tv_shows.title - rating sum, sorted in descending order by the rating
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating FROM tv_show_ratings JOIN tv_shows ON tv_shows.id = tv_show_ratings.show_id GROUP BY tv_shows.title ORDER BY rating DESC;
