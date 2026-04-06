import ipaddress
d=[]
net1=ipaddress.ip_address(f'234.84.23.76')
for mask in range(0, 33):
    net2 = ipaddress.ip_network(f'234.84.23.0/{mask}', 0)
    if net1 in net2:
        print(mask)