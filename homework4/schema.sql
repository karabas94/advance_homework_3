DROP TABLE IF EXISTS tracks;

CREATE TABLE tracks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  artist TEXT NOT NULL,
  genre TEXT NOT NULL,
  lenght INTEGER NOT NULL
);
