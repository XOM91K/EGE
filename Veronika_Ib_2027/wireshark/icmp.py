import re
s = open('icmp.txt').read()
m = re.findall(r'Data:\s+(\w{2,40})', s)
#m = bytes.fromhex(''.join(m))
for x in m:
    if len(x) < 20:
        print(x, bytes.fromhex(bytes.fromhex(x).decode()))
        1cmp_ch4nn3l_c0v3rt leet l33t 1337