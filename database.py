import mysql.connector

mydb = mysql.connector.connect(
    host = "192.168.200.138",
    user = "andrei",
    passwd = "Ar10fiatbti#",
    database = "testdb"
)

my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE testdb")

# my_cursor.execute("SHOW DATABASES")

# for db in my_cursor:
#     print(db[0])

# Create a new table
# my_cursor.execute("CREATE TABLE IF NOT EXISTS users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
# my_cursor.execute("SHOW TABLES")

# for table in my_cursor:
#     print(table[0])

# Insert in tables data
# sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
# record1 = ("Andrei", "apernevan@outlook.com", 38)

# my_cursor.execute(sqlStuff, record1)
# mydb.commit()

# Inser many records
sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
records = [
    ("Tim", "tim@tim.com", 32),
    ("Mary", "mary@mary.com", 22),
    ("Steve", "steve@steveemail.com", 57),
    ("Tina", "time@something.com", 29),
]

my_cursor.executemany(sqlStuff, records)
mydb.commit()