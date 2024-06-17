-- this will list all the shows in the database hbtn_0d_tvshows
-- wach record will display tv_shows.title - tv_shows_genres.genre_id
-- and if a show doesn't have a genre display NULL

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
