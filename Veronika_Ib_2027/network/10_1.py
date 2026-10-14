import ipaddress
steve = ['192.168.10.5', '192.168.10.10', '192.168.10.1']
others = ['192.168.10.70', '192.168.10.40', '192.168.10.41', '192.168.10.65', '192.168.10.32']
for x in range(25, 33):
    net1 = ipaddress.ip_network(steve[0] + f'/{str(x)}', 0)
    net1 = [str(y) for y in net1]
    steveips = [ipaddress.ip_address(y) for y in steve]
    otersips = [ipaddress.ip_address(y) for y in others]
    flag1 = True
    flag2 = True
    for y in steveips:
        y = str(y)
        if y not in net1:
            flag1 = False
    for y in others:
        y = str(y)
        if y in net1:
            flag2 = False
    if flag1 and flag2:
        print(x)