import ipaddress
ct=set()
for A in range(0, 256):
    net=ipaddress.ip_network(f'246.81.65.{A}/255.255.255.224', 0).hosts()
    can = True
    for ip in net:
        a = bin(int(ip))[2:].zfill(32)
        if a[16:24].count('0') <= a[24:].count('0'):
            can = False
            break
    if can:
        ct.add(A)
print(len(set(ct)))