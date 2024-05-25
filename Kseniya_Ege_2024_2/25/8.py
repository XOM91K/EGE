import fnmatch


ctt = 0
for x in range(65001, 10 ** 8):
    g = 0
    cx = 0
    if fnmatch.fnmatch(str(x), '6*97*5?'):
        for f in range(1, int(x ** 0.5) + 1):
            if x % f == 0:
                if f % 2 == 0:
                    cx += 1
                    g += f
                if (x // f) % 2 == 0:
                    cx += 1
                    g += x // f
        if cx >=4:
            print (x, g)
            ctt += 1
        if ctt == 7:
            break
