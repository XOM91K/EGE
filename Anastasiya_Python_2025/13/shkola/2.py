import ipaddress
ct = 0
for x in ipaddress.ip_network('235.86.56.0/255.255.248.0', 0):
    x = bin(int(x))[2:].zfill(32)
    if x[-2:] == '11':
        print(x)
        ct += 1
print(ct)