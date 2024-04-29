def prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    if n < 2:
        return False
    return True
for x in range(41,100):
    s ='0'+'1'*40+'2'*x+'0'
    while '00' not in s:
        s = s.replace('02','101',1)
        s = s.replace('11', '2', 1)
        s = s.replace('012', '30', 1)
        s = s.replace('010', '00', 1)
    if prime(s.count('1')+2*s.count('2') + s.count('3')):
        print(x, s.count('1')+2*s.count('2') + s.count('3'))