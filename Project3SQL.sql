/*
USE mydb;

INSERT INTO Customer VALUES	(69420, "Daniel Yahalom", DATE '2021-4-4', '659-535-5725', "dxy190011@utdallas.edu", "1234************");
INSERT INTO Customer VALUES	(12345, "Noah Fornero", DATE '2001-4-3', "469-420-6969", "nmf190000@utdallas.edu", "1324************");
INSERT INTO Customer VALUES	(54321, "Gaurav Wadhwa", DATE '2001-10-30', "123-456-7891", "blahblah@utdallas.edu", "5555************");
INSERT INTO Customer VALUES	(16256, "Travis Dula", DATE '2002-12-16', "987-999-9099", "travis@utdallas.edu", "1612************");
INSERT INTO Customer VALUES	(43470, "Ke Su", DATE '2000-4-3', "546-345-2856", "kxs130330@utdallas.edu", "9876************");

INSERT INTO Gate VALUES(4556,"C09");
INSERT INTO Gate VALUES(7858,"B02");
INSERT INTO Gate VALUES(8245,"B01");
INSERT INTO Gate VALUES(1847,"A01");

INSERT INTO Pilot VALUES(3512, "Captain Jalal Omer", 1);
INSERT INTO Pilot VALUES(6969, "Captain Daniel Yahalom", 1);
INSERT INTO Pilot VALUES(1512, "Captain Travis Dula", 0);
INSERT INTO Pilot VALUES(1128, "Captain Noah Fornero", 0);
INSERT INTO Pilot VALUES(9346, "Captain Gaurav Wadhwa", 0);

INSERT INTO Flight VALUES(9457, TIME '19:30', DATE '2022-4-4', "KLIA", 5, 6969, 4556);
INSERT INTO Flight VALUES(8712, TIME '13:30', DATE '2022-4-4', "ABZ", 29, 1128, 8245);
INSERT INTO Flight VALUES(1612, TIME '00:00', DATE '2022-7-4', "IIA", 12, 3512, 1847);
INSERT INTO Flight VALUES(4279, TIME '9:30', DATE '2022-9-5', "XYD", 29, 9346, 7858);

Alter TABLE Flight ADD CONSTRAINT Enough_Seats CHECK (Spots_Available >= 0);

INSERT INTO Ticket VALUES(1, 04347, 1612);
INSERT INTO Ticket VALUES(2, 04347, 1612);
INSERT INTO Ticket VALUES(10, 04347, 1612);
INSERT INTO Ticket VALUES(15, 12345, 1612);
INSERT INTO Ticket VALUES(17, 04347, 8712);
INSERT INTO Ticket VALUES(20, 04347, 4279);
INSERT INTO Ticket VALUES(5, 16256, 9457);
INSERT INTO Ticket VALUES(9, 04347, 8712);
INSERT INTO Ticket VALUES(8, 04347, 9457);
INSERT INTO Ticket VALUES(12, 54321, 1612);
INSERT INTO Ticket VALUES(69, 69420, 1612);
INSERT INTO Ticket VALUES(3, 04347, 4279);

SELECT * FROM Customer;
SELECT * FROM Gate;
SELECT * FROM Pilot;
SELECT * FROM Flight;
SELECT * FROM Ticket;
*/

drop database test;

CREATE SCHEMA IF NOT EXISTS test;
use test;
CREATE TABLE IF NOT EXISTS `test`.`Customer` (
  `Cid` INT NOT NULL,
  `Cname` VARCHAR(45) NOT NULL,
  `DOB` DATE NOT NULL CHECK(DOB <= sysdate()),
  `Phone_num` VARCHAR(45) NOT NULL CHECK(Phone_num REGEXP '[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]'),
  `Email` VARCHAR(45) NOT NULL,
  `Payment_Information` VARCHAR(45) NULL CHECK(Payment_Information REGEXP '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
  PRIMARY KEY (`Cid`),
  UNIQUE INDEX `Cid_UNIQUE` (`Cid` ASC))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `test`.`Gate` (
  `Gid` INT NOT NULL,
  `Gate_num` VARCHAR(3) NOT NULL CHECK(Gate_num REGEXP '[A-Z][0-9][0-9]'),
  PRIMARY KEY (`Gid`),
  UNIQUE INDEX `Gid_UNIQUE` (`Gid` ASC))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `test`.`Pilot` (
  `Pid` INT NOT NULL,
  `Pname` VARCHAR(45) NOT NULL,
  `Availability` BIT NOT NULL COMMENT 'True: Means pilot is available to fly\nFalse: Means pilot is not available to fly',
  PRIMARY KEY (`Pid`),
  UNIQUE INDEX `Pid_UNIQUE` (`Pid` ASC))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `test`.`Flight` (
  `Flight_num` INT NOT NULL,
  `Departure Time` DATETIME NOT NULL,
  `Date_of_flight` DATE NOT NULL,
  `Destination` VARCHAR(45) NOT NULL,
  `Spots_Available` INT NOT NULL CHECK (Spots_Available >= 0),
  `Pid` INT NOT NULL,
  `Gid` INT NOT NULL,
  UNIQUE INDEX `Flight_num_UNIQUE` (`Flight_num` ASC),
  INDEX `Pid_idx` (`Pid` ASC) ,
  INDEX `Gid_idx` (`Gid` ASC) ,
  PRIMARY KEY (`Flight_num`),
  CONSTRAINT `Gid`
    FOREIGN KEY (`Gid`)
    REFERENCES `test`.`Gate` (`Gid`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Pid`
    FOREIGN KEY (`Pid`)
    REFERENCES `test`.`Pilot` (`Pid`)
    ON DELETE RESTRICT ON UPDATE CASCADE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `test`.`Ticket` (
  `Tid` INT NOT NULL,
  `Cid` INT NOT NULL,
  `Flight_num` INT NOT NULL,
  PRIMARY KEY (`Tid`),
  UNIQUE INDEX `Tid_UNIQUE` (`Tid` ASC) ,
  INDEX `Cid_idx` (`Cid` ASC),
  INDEX `Flight_num_idx` (`Flight_num` ASC) ,
  CONSTRAINT `Cid`
    FOREIGN KEY (`Cid`)
    REFERENCES `test`.`Customer` (`Cid`)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Flight_num`
    FOREIGN KEY (`Flight_num`)
    REFERENCES `test`.`Flight` (`Flight_num`)
    ON DELETE RESTRICT ON UPDATE CASCADE)
ENGINE = InnoDB;

/*
	These queries populate the database
*/

INSERT INTO Customer VALUES	(69420, "Daniel Yahalom", DATE '2021-4-4', '659-535-5725', "dxy190011@utdallas.edu", "1234569123514523");
INSERT INTO Customer VALUES	(12345, "Noah Fornero", DATE '2001-4-3', "469-420-6969", "nmf190000@utdallas.edu", "1234569123514523");
INSERT INTO Customer VALUES	(54321, "Gaurav Wadhwa", DATE '2001-10-30', "123-456-7891", "blahblah@utdallas.edu", "1234569123514523");
INSERT INTO Customer VALUES	(16256, "Travis Dula", DATE '2002-12-16', "987-999-9099", "travis@utdallas.edu", "1234569123514523");
INSERT INTO Customer VALUES	(43470, "Ke Su", DATE '2000-4-3', "546-345-2856", "kxs130330@utdallas.edu", "1234569123514523");

INSERT INTO Gate VALUES(4556,"C09");
INSERT INTO Gate VALUES(7858,"B02");
INSERT INTO Gate VALUES(8245,"B01");
INSERT INTO Gate VALUES(1847,"A01");

INSERT INTO Pilot VALUES(3512, "Captain Jalal Omer", 1);
INSERT INTO Pilot VALUES(6969, "Captain Daniel Yahalom", 1);
INSERT INTO Pilot VALUES(1512, "Captain Travis Dula", 0);
INSERT INTO Pilot VALUES(1128, "Captain Noah Fornero", 0);
INSERT INTO Pilot VALUES(9346, "Captain Gaurav Wadhwa", 0);

INSERT INTO Flight VALUES(9457, TIME '19:30', DATE '2022-4-4', "KLIA", 5, 6969, 4556);
INSERT INTO Flight VALUES(8712, TIME '13:30', DATE '2022-4-4', "ABZ", 29, 1128, 8245);
INSERT INTO Flight VALUES(1612, TIME '00:00', DATE '2022-7-4', "IIA", 12, 3512, 1847);
INSERT INTO Flight VALUES(4279, TIME '9:30', DATE '2022-9-5', "XYD", 29, 9346, 7858);
INSERT INTO Flight VALUES(4595, TIME '9:30', DATE '2022-4-3', "DFW", 0, 9346, 7858);

INSERT INTO Ticket VALUES(15, 12345, 1612);
INSERT INTO Ticket VALUES(5, 16256, 9457);
INSERT INTO Ticket VALUES(12, 54321, 1612);
INSERT INTO Ticket VALUES(69, 69420, 1612);
INSERT INTO Ticket VALUES(1, 43470, 1612);
INSERT INTO Ticket VALUES(2, 43470, 1612);
INSERT INTO Ticket VALUES(3, 43470, 4279);
INSERT INTO Ticket VALUES(8, 43470, 9457);
INSERT INTO Ticket VALUES(9, 43470, 8712);
INSERT INTO Ticket VALUES(10, 43470, 1612);
INSERT INTO Ticket VALUES(17, 43470, 8712);
INSERT INTO Ticket VALUES(20, 43470, 4279);
INSERT INTO Ticket VALUES(91, 43470, 4595);
/*
	These queries show the tables
*/

SELECT * FROM Customer;
SELECT * FROM Gate;
SELECT * FROM Pilot;
SELECT * FROM Flight;
SELECT * FROM Ticket;

/*
	These queries test the constraints
*/
INSERT INTO Customer VALUES	(69420, "Daniel Yahalom", DATE '2022-4-4', '659-535-5725', "dxy190011@utdallas.edu", "1234569123514523");
INSERT INTO Customer VALUES	(69420, "Daniel Yahalom", DATE '2021-4-4', '659-535-5a25', "dxy190011@utdallas.edu", "1234569123514523");
INSERT INTO Customer VALUES	(69420, "Daniel Yahalom", DATE '2021-4-4', '659-535-5725', "dxy190011@utdallas.edu", "123456912a514523");
INSERT INTO Gate VALUES(4556, "C9");

/*
	Views
*/
CREATE VIEW TicketsToday AS
SELECT T.Tid
FROM Ticket T
JOIN Flight F
ON T.Flight_num = F.Flight_num
WHERE F.Date_of_flight = current_date();
SELECT * FROM TicketsToday;

CREATE VIEW Customer_Info AS
SELECT Cid, Cname, DOB, Email
FROM Customer;
SELECT * FROM Customer_Info;

Create VIEW AvailableFlights AS
SELECT F.Flight_num, F.Destination, F.Spots_available
FROM Flight F
WHERE F.Spots_available > 0;
SELECT * FROM AvailableFlights;

Create VIEW TicketsByCID AS
Select COUNT(T.Tid), C.Cid
FROM Ticket T, Customer C
WHERE T.Cid = C.Cid
GROUP BY C.Cid;
SELECT * FROM TicketsByCID;

DROP VIEW TicketsByCID;

Create VIEW FlightsByGate AS
Select COUNT(F.Flight_num), G.Gate_num
FROM Flight F, Gate G
WHERE F.Gid = G.Gid
GROUP BY G.Gate_num;
SELECT * FROM FlightsByGate;

DROP VIEW FlightsByGate;
/*
	Queries
*/
SELECT cname, Flight_num  
FROM Customer c
JOIN Ticket t
Where t.cid = c.cid;

SELECT Gate_num, Flight_num  
FROM Gate g
JOIN Flight f
Where g.gid = f.gid;

SELECT P.Pname, F.Flight_num, F.Date_of_flight
FROM Pilot P, Flight F
WHERE P.Pid = F.Pid;
