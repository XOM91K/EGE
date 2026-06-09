import ipaddress
for x in ipaddress.ip_network('46.29.170.214/255.255.128.0',0).hosts():
    d = x
    x = sorted([int(d) for d in str(x).split('.')])
    if x[0] + x[1] + x[2] == x[3]:
        print(d)