/*
Leilani Sears
CSE 412
ER Diagram -> Relational Translation

Relations will be edited as GUI is developed.
 */

CREATE TABLE Playlist(
  playlistID INT PRIMARY KEY,
  followers INT, 
  ownerName VARCHAR(50),
  dateCreated DATE,
  playlistLink VARCHAR(100)
);

CREATE TABLE Song(
  songID INT PRIMARY KEY,
  artistName VARCHAR(50),
  songName VARCHAR(50),
  songLink VARCHAR(100),
  duration INTERVAL HOUR TO MINUTE
);

CREATE TABLE UserEntity(
  userID INT PRIMARY KEY,
  likes INT,
  shares INT,
  playlistCount INT,
  country VARCHAR(50),
  displayName VARCHAR(50),
  image VARCHAR(100),
  playlists INT
);
