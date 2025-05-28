import ipaddress
ct = 0
for i in ipaddress.ip_network('211.46.0.0/255.255.128.0', 0):
    n = bin(int(i))[2:].zfill(32)
    if n.count('1') % 4 == 0 and n[-2:] == '11':
        ct += 1
print(ct)