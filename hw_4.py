#import mysql.connector
#
#conn = mysql.connector.connect(
#        user='root',
#        password='password',
#        host='127.0.0.1',
#        database='mydb'
#        )
#
#cursor = conn.cursor()

print('Hello user! Are you are (c)ustomer, (p)ilot, or (a)dmin?')
match list(input('I am a: ').lower()):
    case ['c', *_]:
        print('Hello customer!')
        ID = input('Enter your ID to get your information ')
        #cursor.execute(f'SELECT * FROM Customer WHERE Customer.cid = {ID}')
    case ['p', *_]:
        print('Hello pilot!')
    case ['a', *_]:
        print('Hello admin!')



# cursor.close()
# conn.close()
