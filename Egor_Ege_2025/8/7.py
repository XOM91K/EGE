cnt = 0
import itertools
for i in itertools.product("0123456789ab", repeat = 7):
    w = "".join(i)
    if w[0] != "0" and w.count('b') == 2:
        w = w.replace("3", "1")
        w = w.replace("5", "1")
        w = w.replace("7", "1")
        w = w.replace("9", "1")
        w = w.replace("b", "1")
        w = w.replace("2", "0")
        w = w.replace("4", "0")
        w = w.replace("6", "0")
        w = w.replace("8", "0")
        w = w.replace("a", "0")
        if "00" not in w and "11" not in w:
            cnt += 1
print(cnt)