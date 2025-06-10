import ipaddress
ct = 0
for x in ipaddress.ip_network('112.208.0.0/255.255.224.0', 0):
    x = bin(int(x))[2:].zfill(32)
    if x[-3:] == '000' or x[-3:] == '111':
        print(x)
        ct += 1
print(ct)