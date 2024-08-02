count2 = 0
for A in range(-100, 100):
    count = 0
    d = [(1, 2), (11, 2), (1, 12), (11, 12), (-11, -12),
         (-11, 12), (-12, 11), (10, 10), (10, 5)]
    for s, t in d:
        if not((s > 10) or (t > A)):
            count += 1
    if count == 3:
        count2 += 1
print(count2)
#кортеж ()
#спичок []