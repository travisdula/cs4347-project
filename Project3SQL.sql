USE mydb;

INSERT INTO Customer VALUES	(69420, "Daniel Yahalom", DATE '2021-4-3', "659-535-5725", "dxy190011@utdallas.edu", "1234************"),
							(12345, "Noah Fornero", DATE '2001-4-3', "469-420-6969", "nmf190000@utdallas.edu", "1324************"),
							(54321, "Gaurav Wadhwa", DATE '2001-10-30', "123-456-7891", "blahblah@utdallas.edu", "5555************"),
                            (16256, "Travis Dula", DATE '2002-12-16', "987-999-9099", "travis@utdallas.edu", "1612************"),
                            (43470, "Ke Su", DATE '2000-4-3', "546-345-2856", "kxs130330@utdallas.edu", "9876************");

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
