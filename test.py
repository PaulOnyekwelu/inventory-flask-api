import sqlite3
import os

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

query = '''
  CREATE TABLE users
  (
    id int AUTO_INCREMENT,
    username varchar(50),
    password text,
    PRIMARY KEY (id)
  )
  '''

cursor.execute(query)

add = 'INSERT INTO users VALUES (?, ?, ?)'
user_list = [
    (1, "silanka", "asdf"),
    (2, "david", "1234"),
    (3, "linda", "1111"),
]
result = cursor.executemany(add, user_list)
print(result)
connection.commit()
connection.close()
