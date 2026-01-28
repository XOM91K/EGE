import ipaddress
ct = 0
for A in range(0, 256):
    can = True
    q1 = str(list(ipaddress.ip_network(f'246.81.65.{A}/255.255.255.224', 0))[0])
    q2 = str(list(ipaddress.ip_network(f'246.81.65.{A}/255.255.255.224', 0))[-1])
    if f'246.81.65.{A}' not in q1 and f'246.81.65.{A}' not in q2:
        for x in list(ipaddress.ip_network(f'246.81.65.{A}/255.255.255.224', 0))[1:-1]:
            x = bin(int(x))[2:].zfill(32)
            if x[16:24].count('0') <= x[-8:].count('0'):
                can = False
                break
        if can:
            print(A)
            ct += 1
print(ct)