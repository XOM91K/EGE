import ipaddress
ct = 0
d =ipaddress.ip_network('172.140.68.0/255.255.248.0', 0)
print(d)
for x in ipaddress.ip_network('172.140.68.0/255.255.248.0', 0):
    r = bin(int(x))[2:].zfill(32)
    print(r)
    if r.count('0') > 15:
        ct += 1
print(ct)