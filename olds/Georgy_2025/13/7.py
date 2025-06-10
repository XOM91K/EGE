import ipaddress
for mask in range(15, 33):
    ip1 = ipaddress.ip_network(f'211.188.211.49/{mask}', 0)
    ip2 = ipaddress.ip_network(f'211.188.200.115/{mask}', 0)
    if ip1 == ip2:
        ct = 0
        for y in ip1:
            y = bin(int(y))[2:].zfill(32)
            if y.count('1') % 2 != 0:
                ct += 1
        print(ct)
# print(ip1)
# print(list(ip1))