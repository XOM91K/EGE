otv = 0
for i in range(3, 1000):
    x = "3" + "5"*i
    sm = 0
    while "25" in x or "355" in x or "555" in x:
        if "25" in x:
            x = x.replace("25", "32", 1)
        if "355" in x:
            x = x.replace("355", "25", 1)
        if "555" in x:
            x = x.replace("555", "3", 1)
    for j in x:
        sm += int(j)
    for j in range(2, int(sm**0.5)+1):
        if sm % j == 0:
            break
    else:
        otv += 1
print(otv)