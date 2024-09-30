import ipaddress
ct = 0
for A in range(0, 256):
        can = True
        net = ipaddress.IPv4Network('246.81.65.' + (str(A)) + '/255.255.255.224', False).network_address
        print(net)
        for x in ipaddress.ip_network(str(net) + '/255.255.255.224', False):
            x = f'{x:b}'
            if x[16:24].count('0') <= x[24:32].count('0'):
                can = False
            print(x[16:24], x[24:32])
            print(x)
        if can == True:
            ct += 1
print(ct)