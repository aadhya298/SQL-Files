
CREATE TABLE City (

City_Id INTEGER PRIMARY KEY,

City_Name TEXT NOT NULL

);

CREATE TABLE Venue (

Venue_Id INTEGER PRIMARY KEY,

Venue_Name TEXT NOT NULL,

City_Id INTEGER,

FOREIGN KEY (City_Id) REFERENCES City(City_Id)

);

CREATE TABLE Team (

Team_Id INTEGER PRIMARY KEY,

Team_Name TEXT NOT NULL

);

CREATE TABLE Match (

Match_Id INTEGER PRIMARY KEY,

Season_Id INTEGER NOT NULL,

Venue_Id INTEGER,

Match_Winner INTEGER,

FOREIGN KEY (Venue_Id) REFERENCES Venue(Venue_Id),

FOREIGN KEY (Match_Winner) REFERENCES Team(Team_Id)

);
#cities

INSERT INTO City VALUES

(1, 'Mumbai'),

(2, 'Delhi'),

(3, 'Chennai');

# Venue
INSERT INTO Venue VALUES

(1, 'Wankhede Stadium', 1),

(2, 'Feroz Shah Kotla', 2),

(3, 'Chepauk Stadium', 3);
#Teams

INSERT INTO Team VALUES

(1, 'Mumbai Indians'),

(2, 'Chennai Super Kings'),

(3, 'Delhi Capitals');
#Matches

INSERT INTO Match VALUES

(101, 2023, 1, 1),

(102, 2023, 2, 3),

(103, 2024, 3, 2),

(104, 2024, 1, 1);