import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "test.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

# sql_command = """
#         CREATE TABLE test (
#             user_id  INTEGER PRIMARY KEY,
#             username TEXT NOT NULL
#         );
#     """

# cursor.execute(sql_command)

cursor.execute("INSERT INTO test (username) VALUES ('kim');")
connection.commit()

# cursor.execute("SELECT * FROM users;")
# user = cursor.fetchall()
# print(user)

#cursor.execute("DROP TABLE friends;")

connection.close()