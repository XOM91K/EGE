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
    nS = {}
    for x in albums:
        for y in artist_ids:
            cur.execute(f"""SELECT 
            AlbumId FROM Album 
            WHERE ArtistId = {y} AND AlbumId = {x}""")
            nameTrack = cur.fetchone()
            if y not in nS:
                nS[y] = []
            nS[y].append(nameTrack)
    for x in nS:
        nS[x] = [x[0] for x in nS[x] if x is not None]
    name_albums = []
    for y in nS:
        for x in range(len(nS[y])):
            cur.execute(f"""SELECT Title 
            FROM Album 
            WHERE AlbumId = {nS[y][x]}""")
            nS[y][x] = cur.fetchone()[0]
    for x in nS:
        nS[x] = sorted(nS[x])
        if len(nS[x]) > 0:
            for y in nS[x]:
                print(y)