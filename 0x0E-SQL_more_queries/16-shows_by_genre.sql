-- List all shows and all genres linked to each show
-- If a show doesn’t have a genre, display NULL in the genre column,  display: tv_shows.title - tv_genres.name, sorted in ascending order by the show title and genre name
SELECT tv_shows.title, tv_genres.name FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id ORDER BY tv_shows.title, tv_genres.name;
