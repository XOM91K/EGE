import ipaddress
ct = 0
for x in ipaddress.ip_network('123.222.111.192/255.255.255.248', 0):
    x = bin(int(x))[2:].zfill(32)
    if x[-8:].count('1') % 3 != 0:
        ct += 1
print(ct)