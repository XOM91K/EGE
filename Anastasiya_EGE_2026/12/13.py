mx = []
for x in range(8000, 12000):
    for y in range(1000, 3000):
        if len(str(x * 8 + y * 7)) == 5:
            mx.append((x * 8 + y * 7) + x + y)
print(max(mx))