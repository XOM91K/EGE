import sqlite3
name = input()
with sqlite3.connect('Chinook_Sqlite.sqlite') as con:
    cur = con.cursor()
    cur.execute(f"SELECT GenreId FROM Genre WHERE Name = '{name}'")
    id_name = cur.fetchone()
    cur.execute(f"SELECT TrackId FROM Track WHERE GenreId = {id_name[0]}")
    albums = cur.fetchall()
    name_Track_sets = []
    for x in albums:
        cur.execute(f"SELECT Name FROM Track WHERE GenreId = {x[0]}")
        nameTrack = cur.fetchall()
        nameTrack = [g[0] for g in nameTrack]
        name_Track_sets.extend(nameTrack)
    name_Track_sets = sorted(name_Track_sets, key=lambda d: (d[0]))
    for x in name_Track_sets:
        print(x)
