-- List all shows in hbtn_0d_tvshows with at least one genre linked
-- tv_shows.title - tv_show_genres.genre_id, sorted in ascending order by tv_shows.title and tv_show_genres.genre_id, only one SELECT
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id WHERE tv_show_genres.genre_id IS NOT NULL ORDER BY tv_shows.title, tv_show_genres.genre_id;
