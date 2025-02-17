import ipaddress
ct =0
for A in range(0, 256):
    ip1 = ipaddress.ip_network(f'246.81.65.{A}/255.255.255.224', 0)
    can = True
    ip = list(ip1)
    for x in ip:
        x = bin(int(x))[2:]
        if x[16:24].count('0') <= x[-8:].count('0'):
            can = False
            break
    if can:
        print(A)
        ct += 1
print(ct)