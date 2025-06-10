for x in range(206,10**8,206):
    s = str(x)
    if s[:3] == '123' and int(s[-4]) % 2 != 0 and int(s[-3]) % 2 == 0 and s[-2:] == '56':
        print(x, x//206)