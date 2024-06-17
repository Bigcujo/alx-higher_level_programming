-- this script shows all the tv shows in the data base called hbtn_0d_tvshows thatare linked to a genre.
-- each record will display: tv_shows.title - tv_shows_genres.genre_id

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
