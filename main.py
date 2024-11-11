for n in range(154, 1000):
    s = bin(n)[2:] # перевод в двоичную систему
    s = str(s)
    for i in range(3):
        if s.count("1") == s.count("0"):
            s += s[-1]
        elif s.count("1") > s.count("0"):
            s += "0"
        else:
            s += "1"
    r = int(s, 2) # перевод в десятичную систему
    if r % 7 == 0:
        print(n)
        break