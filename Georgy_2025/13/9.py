import ipaddress
ct = 0
for x in ipaddress.ip_network("172.16.80.0/255.255.248.0",0):
    x = bin(int(x))[2:].zfill(32)
    if x.count('1')%2 != 0:
        ct += 1
print(ct)