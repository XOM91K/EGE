import ipaddress
ct = 0
for x in ipaddress.ip_network('250.135.101.80/255.255.255.248', False):
    x = bin(int(x))[2:].zfill(32)
    if x.count('0') % 3 == 0:
        ct += 1
print(ct)