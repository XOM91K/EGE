# import sqlite3 as sq
# con = sq.connect("saper.db")
# cur = con.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS users(
# user_id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT NOT NULL,
# gender INTEGER DEFAULT 1,
# old INTEGER,
# score INTEGER NOT NULL DEFAULT 0)""")
# cur.execute("INSERT INTO users (name, gender, old, score) VALUES('Мария', 1, 32, 400)")
#
# cur.execute("SELECT rowid,* FROM users")
# print(cur.fetchall())
# con.commit()
# con.close()
# print(9 / 0)