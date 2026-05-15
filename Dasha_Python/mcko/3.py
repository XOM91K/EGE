s = 1
for i in range(3, 31):
    if i % 5 == 0 or i % 7 == 0:
        print(i)
        s = s + 3
    # if i % 10 == 0:
    #     s = s - 2
print('---')
print(s)