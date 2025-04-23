import ipaddress
for x in ipaddress.ip_network('158.214.121.40/255.255.255.224', 0):
    #x=bin(int(x))[2:].zfill(32)
    print(x)