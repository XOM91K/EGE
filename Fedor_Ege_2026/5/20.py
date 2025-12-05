for n in range(1, 10000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = r + '0'
        r =  '10' + r[2:]
    else: # c противоположным условием ответ не правильный
        r = r + '1'
        r = '11' + r[2:]
    r = int(r, 2)
    if n > 27:
        print(r)