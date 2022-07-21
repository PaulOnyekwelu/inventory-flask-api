import sqlite3
import app.utils.constants as constants

connection = sqlite3.connect(constants.DB_URI)
cursor = connection.cursor()

users_query = """CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username VARCHAR(50),
        password TEXT
    )
    """

cursor.execute(users_query)
connection.commit()
connection.close()
