CREATE TABLE US_STATES (
	ID int(11) NOT NULL AUTO_INCREMENT,
	STATE_CODE char(2) NOT NULL,
	STATE_NAME varchar(50) NOT NULL,
	PRIMARY KEY (ID)
);

CREATE TABLE US_CITIES (
	ID int(11) NOT NULL AUTO_INCREMENT,
	ID_STATE int(11) NOT NULL,
	CITY varchar(50) NOT NULL,
	COUNTY varchar(50) NOT NULL,
	LATITUDE double NOT NULL,
	LONGITUDE double NOT NULL,
	PRIMARY KEY (ID),
    FOREIGN KEY (ID_STATE) REFERENCES US_STATES(ID)
);

CREATE TABLE College (
    Name varchar(255)
    Address varchar(255),
    Population int,
    City varchar(255),
    State varchar(255),
    Country varchar(255),
    Zip int
);

create table Stats(
  StatsID int primary key,
  MIN real,
  PTS real,
  FG real,
  ThreePT real,
  REB real,
  AST real,
  STL real,
  BLK real
);

create table Team(
  TeamName varchar(255) primary key,
  Stadium varchar(255),
  CityID int,
  Seat_Cap int,
  Open_year int,
  FOREIGN KEY (CityID) REFERENCES US_CITIES(ID)
);

create table movie_and_genre_sql(
  id int primary key,
  movie varchar(255) NOT NULL,
  genre varchar(255) NOT NULL
);

create table Draft(
  Draft_ID varchar(255) primary key,
  Draft_year varchar(255),
  Draft_round varchar(255),
  Draft_number varchar(255),
);

create table Player(
  Player_ID int primary key,
  Name varchar(255),
  Height varchar(10),
  Weight real,
  Age int,
  Country varchar(255),
  TeamName varchar(255),
  CollegeName varchar(255),
  Movie_ID int
);
