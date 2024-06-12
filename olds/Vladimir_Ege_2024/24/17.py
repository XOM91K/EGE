s = open('17.txt').readline()
for x in 'FAIL':
    k = 1
    while x * k in s:
        k += 1
    print(k - 1)