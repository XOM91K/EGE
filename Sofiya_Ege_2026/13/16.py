import ipaddress
d=[]

for mask in range(0, 33):
    net1 = ipaddress.ip_network(f'234.84.23.76/{mask}', 0)
    #net2 = ipaddress.ip_network(f'234.84.23.0/{mask}', 0)
    print(net1)