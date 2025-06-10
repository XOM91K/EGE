import ipaddress
ct = 0
for x in ipaddress.ip_network('112.208.0.0/255.255.224.0', 0):
    x = bin(int(x))[2:].zfill(32)
    if x[-1] == x[-2] == x[-3]:
        ct += 1
print(ct)