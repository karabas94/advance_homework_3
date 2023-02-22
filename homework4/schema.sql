DROP TABLE IF EXISTS tracks;
DROP TABLE IF EXISTS genres;

create table genres(
    id integer primary key autoincrement,
    title text not null
);

CREATE TABLE tracks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  artist TEXT NOT NULL,
  genre_id integer not null,
  lenght INTEGER NOT NULL,
  FOREIGN KEY (genre_id) REFERENCES genres(id)
);
