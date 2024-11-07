import sqlite3 as sq
con = sq.connect("saper.db")
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
user_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
gender INTEGER DEFAULT 1,
old INTEGER,
score INTEGER NOT NULL DEFAULT 0)""")
cur.execute("""INSERT INTO users (user_id, name, gender, old, score) VALUES(6, 'Петя', 1000, 25, 200)""")
cur.execute("SELECT * FROM users")
print(cur.fetchall())
con.close()