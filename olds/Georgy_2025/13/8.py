import ipaddress
ct = 0
for x in ipaddress.ip_network("112.160.0.0/255.240.0.0", 0):
    x = bin(int(x))[2:].zfill(32)
    if x.count("1")%5 == 0:
        ct += 1
print(ct)