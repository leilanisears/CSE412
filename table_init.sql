/*
Leilani Sears
CSE 412
ER Diagram -> Relational Translation

Relations will be edited as GUI is developed.
 */

CREATE TABLE Playlist(
  playlistID INT PRIMARY KEY,
  followers INT, 
  ownerName VARCHAR(50) NOT NULL,
  dateCreated DATE,
  playlistLink VARCHAR(100) NOT NULL
);

CREATE TABLE Song(
  songID INT PRIMARY KEY,
  artistName VARCHAR(50) NOT NULL,
  songName VARCHAR(50) NOT NULL,
  songLink VARCHAR(100) NOT NULL,
  duration INTERVAL HOUR TO MINUTE
);

CREATE TABLE UserEntity(
  userID INT PRIMARY KEY,
  likes Playlist[],
  shares Playlist[],
  playlistCount INT,
  country VARCHAR(50),
  displayName VARCHAR(50) NOT NULL,
  image VARCHAR(100),
  playlists Playlist[]
);
