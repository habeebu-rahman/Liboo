import sqlite3

connection = sqlite3.connect('database.db')  # change to your DB file name
cursor = connection.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

# Example: show data from user table
cursor.execute("ALTER TABLE donated_book DROP COLUMN date;")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()