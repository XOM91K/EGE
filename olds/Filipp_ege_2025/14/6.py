sis = "0123456789ABCDEFGHIJKLMNOPQRST"
for x in sis:
    for y in sis:
        if (int(f"B{y}{x}6R94E{x}", 30) + int(f"M{y}KGN{x}", 30)) % 10 == 0:
            print(y,  (int(f"B{y}{x}6R94E{x}", 30) + int(f"M{y}KGN{x}", 30)) // 10)