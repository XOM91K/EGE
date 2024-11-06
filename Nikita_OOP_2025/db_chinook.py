import sqlite3
name = input()
with sqlite3.connect('Chinook_Sqlite.sqlite') as con:
    cur = con.cursor()
    cur.execute(f"SELECT ArtistId FROM Artist WHERE Name = '{name}'")
    id_name = cur.fetchone()
    cur.execute(f"SELECT AlbumId FROM Album WHERE ArtistId = {id_name[0]}")
    albums = cur.fetchall()
    name_Track_sets = set()
    for x in albums:
        cur.execute(f"SELECT Name FROM Track WHERE AlbumId = {x[0]}")
        nameTrack = cur.fetchall()
        nameTrack = [g[0] for g in nameTrack]
        name_Track_sets.update(nameTrack)
    name_Track_sets = sorted(name_Track_sets)
    for x in name_Track_sets:
        print(x)
