import ipaddress
ct = 0
for x in ipaddress.ip_network('171.128.0.0/255.128.0.0', 0):
    x = bin(int(x))[2:].zfill(32)
    if x[0:16].count('1') < x[16:].count('1'):
        ct += 1
print(ct)
