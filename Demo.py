import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Testing#1", database="test")

mycursor = mydb.cursor()

"""
# Part A retrieves information from database with prepared statements
print('Hello customer!')
ID = input('Enter your ID to get your information: ')

mycursor.execute(f'SELECT * FROM Customer WHERE Customer.cid = {ID}')

for i in mycursor:
    print(i)
"""
"""
# Part B updates a pilot's availability
ID = input('Please input your pilot ID to mark yourself as unavailable: ')

mycursor.execute(f'UPDATE Pilot SET Availability=0 WHERE Pilot.pid = {ID}')

mycursor.execute(f'SELECT * FROM Pilot WHERE Pilot.pid = {ID}')
for i in mycursor:
    print(i)
"""
"""
# Part C Drops table from database
print('Hello customer!')
ID = input('Enter your ID to get your information: ')

mycursor.execute(f'SELECT * FROM Customer WHERE Customer.cid = 1; Drop TABLE Ticket;')
for i in mycursor:
    print(i)
"""

mycursor = mydb.cursor(prepared=True)

sql_prepared_query = """SELECT * FROM Customer WHERE Customer.Cid = %s; """

# retreive name from user...
print('Hello customer!')
ID = (input('Enter your ID to get your information: '))
tuple1 = (ID, )

mycursor.execute(sql_prepared_query, tuple1)

for i in mycursor:
    print(i)