import ipaddress
sp1 = []
sp2 = []
for x in ipaddress.ip_network('192.168.56.192/255.255.255.192', False):
    sp1.append(x)
for x in ipaddress.ip_network('192.168.56.208/255.255.255.240', False):
    sp2.append(x)
print(len(sp1))
print(len(sp2))
ct = 0
for x in sp1:
    if x not in sp2:
        ct += 1
print(64-16, ct)