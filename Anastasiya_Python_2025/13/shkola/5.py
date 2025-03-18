import ipaddress
ct = 0
for x in ipaddress.ip_network('87.226.26.72/255.255.255.252', 0):
    x = bin(int(x))[2:].zfill(32)
    if x.count('0') % 2 == 0:
        ct += 1
print(ct)