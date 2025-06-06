import ipaddress
p = []
for i in range(33):
    h = ipaddress.ip_network(f"3.120.77.205/{i}", 0)
    h1 = ipaddress.ip_network(f"3.120.77.131/{i}", 0)
    if h != h1:
        g = i * '1' + (32 - i) * '0'
        k = int(g[-8:], 2)
        p.append(k)
print(p)