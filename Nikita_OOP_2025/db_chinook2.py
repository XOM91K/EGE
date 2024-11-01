import sqlite3
name = input()
with sqlite3.connect('Chinook_Sqlite.sqlite') as con:
    cur = con.cursor()
    cur.execute(f"SELECT GenreId FROM Genre WHERE Name = '{name}'")
    id_name = cur.fetchone()
    cur.execute(f"SELECT AlbumId FROM Track WHERE GenreId = {id_name[0]}")
    albums = [int(x[0]) for x in list(set(cur.fetchall()))]
    cur.execute(f"SELECT ArtistId FROM Artist")
    artist_ids = [int(x[0]) for x in cur.fetchall()]
    name_Track_sets = {}
    for x in albums:
        for y in artist_ids:
            cur.execute(f"SELECT AlbumId FROM Album WHERE ArtistId = {y} AND AlbumId = {x}")
            nameTrack = cur.fetchone()
            if y not in name_Track_sets:
                name_Track_sets[y] = []
            name_Track_sets[y].append(nameTrack)
    for x in name_Track_sets:
        name_Track_sets[x] = [x[0] for x in name_Track_sets[x] if x is not None]
    name_albums = []
    for y in name_Track_sets:
        for x in range(len(name_Track_sets[y])):
            cur.execute(f"SELECT Title FROM Album WHERE AlbumId = {name_Track_sets[y][x]}")
            name_Track_sets[y][x] = cur.fetchone()[0]
    for x in name_Track_sets:
        name_Track_sets[x] = sorted(name_Track_sets[x])
        if len(name_Track_sets[x]) > 0:
            for y in name_Track_sets[x]:
                print(y)