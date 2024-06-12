s = open('6.txt').readline()
# F A I L
for x in 'FAIL':
    k = 1
    while x * k in s:
        k += 1
    print(x, k - 1)