import sqlite3 as sq #alias
con = sq.connect("saper.db")
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
user_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
gender INTEGER DEFAULT 1,
old INTEGER,
score INTEGER NOT NULL DEFAULT 100
)""")
#cur.execute("INSERT INTO users(name, gender, old, score) values('Жанна', 1, 16, 1490)")
# cur.execute("SELECT * FROM users ORDER BY score DESC LIMIT 3")
#cur.execute("DELETE FROM users WHERE user_id=3")
# d = cur.fetchall()
# for s in d:
#     print(s)
con.commit()
con.close()