count = 0
for x in range(1_100_000_000, 1_987_653_210+1):
    if x%16 in [10,15] or x%8 in [0,3]:
        count += 1
print(count)