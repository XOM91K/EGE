import ipaddress
ct = 0
for x in ipaddress.ip_network('211.188.211.49/255.255.224.0',False):
    x = bin(int(x))[2:].zfill(32)
    if x.count('1') % 2 !=0 :
        ct += 1
print(ct)