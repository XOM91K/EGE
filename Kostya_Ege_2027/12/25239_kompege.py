def cmd1(s):
    return s
def cmd2(s):
    return s.replace('1', '0', 1)
def cmd3(s):
    return s.replace('0', '1', 1)
def cmd4(s):
    return s
def cmd5(s):
    return s
def cmd6(s):
    return s
s = '0'
cmd = 6
for n in range(1, 1000):
    if s.count('0') == 200:
        print(n)
    s = '0' + s
    if cmd == 6:
        s = cmd6(s)
        cmd = 3
        continue
    if cmd == 3:
        s = cmd3(s)
        cmd = 6
        continue
