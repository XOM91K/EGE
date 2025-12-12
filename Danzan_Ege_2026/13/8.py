import ipaddress
ct = 0
for x in ipaddress.ip_network('222.121.128.0/255.255.224.0', 0):
    x = bin(int(x))[2:].zfill(32)
    if x[-2] == x[-1]:
        ct += 1
        print(x)
print(ct)