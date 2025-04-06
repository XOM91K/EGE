import ipaddress
#3.8
for x in ipaddress.ip_network('250.135.101.80/255.255.255.248', 0):
    x = bin(int(x))[2:].zfill(32)
    if x.count('0') % 3 == 0:
        print(x)