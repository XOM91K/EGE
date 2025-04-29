import ipaddress
ct = 0
for x in ipaddress.ip_network('192.168.108.157/255.255.255.192', 0):
    mask = ipaddress.ip_address('255.255.255.192')
    mask = bin(int(mask))[2:].zfill(32)
    x = bin(int(x))[2:].zfill(32)
    print(x, mask)
print(ct)