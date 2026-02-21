import itertools

ct = 0
for x in itertools.permutations('ХЛЕБНЫЙМЯКИШ', 7):
    x = ''.join(x)
    if x[0] == "Х":
        x = x.replace("Б", "1")
        x = x.replace("К", "1")
        x = x.replace("Ш", "1")
        x = x.replace("Ы", "2")
        x = x.replace("И", "2")
        if x[3] == "1" or x[3] == "2":
            x = x.replace("Х", "1")
            x = x.replace("Л", "1")
            x = x.replace("Н", "1")
            x = x.replace("М", "1")
            x = x.replace("Й", "1")
            x = x.replace("Я", "2")
            if x.count("11") == 0:
                ct += 1
print(ct)
