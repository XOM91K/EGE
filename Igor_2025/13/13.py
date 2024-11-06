import ipaddress
ct = 0
set1 = set()
set2 = set()
for x in ipaddress.ip_network('192.168.56.192/255.255.255.192', False):
    x = str(x)
    set1.add(x)

for x in ipaddress.ip_network('192.168.56.208/255.255.255.240', False):
    x =str(x)
    set2.add(x)
ct = 0
for x in list(set1):
    if x not in list(set2):
        ct += 1
for x in list(set2):
    if x not in list(set1):
        ct += 1
print(ct)