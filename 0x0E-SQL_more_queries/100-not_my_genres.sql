-- List all genres not linked to the show Dexter
-- tv_shows table contains only one record where title = Dexter (but the id can be different), display: tv_genres.name,  sorted in ascending order by the genre name,maximum of two SELECT
SELECT tv_genres.name FROM tv_genres WHERE tv_genres.name NOT IN (SELECT tv_genres.name FROM tv_show_genres JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_shows.title = 'Dexter') ORDER BY tv_genres.name;
