import mysql.connector

# connect to the database server
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Krishna@123',
        database='flights'
    )
    mycursor = conn.cursor()
    print('Connection done')

except Exception as e:
    print(f'Error: {e}')
    print('No Connection')

# create a database on the db server
# mycursor.execute("CREATE DATABASE indigo")
# conn.commit()

# create a table
# airport -> airport_id | code | name
# mycursor.execute("""
# CREATE TABLE airport(
# airport_id integer PRIMARY KEY,
# code varchar(10) NOT NULL ,
# city varchar(50) NOT NULL,
# name varchar(50) NOT NULL
# )
# """)
# conn.commit()

# insert data to the table
# mycursor.execute("""
#         INSERT INTO airport VALUES
#         (1,'DEL' , 'New Delhi' , 'IGIA'),
#         (2,'CCU' , 'Kolkata' , 'NSCA'),
#         (3 , 'BOM' , 'Mumbai' , 'CSMA')
# """)
# conn.commit()

#search retrieve
mycursor.execute("SELECT * FROM airport where airport_id>1")
data = mycursor.fetchall()
print(data)

for i in data:
    print(i[3])

# update
mycursor.execute(""" 
update airport 
set name = 'Bombay' 
where airport_id = 3
""")
conn.commit()


mycursor.execute("SELECT * FROM airport ")
data = mycursor.fetchall()
print(data)

# DELETE
mycursor.execute(""" DELETE FROM airport WHERE airport_id = 3
""")
conn.commit()
mycursor.execute("SELECT * FROM airport ")
data = mycursor.fetchall()
print(data)
