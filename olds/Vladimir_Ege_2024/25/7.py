sm = 0
for x in range(1686, 13277):
    for y in str(x):
        if int(y) % 2 == 0:
            break
    else:
        for z in str(x):
            sm += int(z)
print(sm)