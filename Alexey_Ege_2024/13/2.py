import ipaddress
ct = 0
for x in ipaddress.ip_network('192.168.32.160/255.255.255.240'):
    x = bin(int(x))
    print(x)
    if x.count('0') - 1 > 21:
        ct += 1
print(ct)