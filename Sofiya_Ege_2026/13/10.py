import ipaddress
for mask in range(15, 33):
    net = ipaddress.ip_network(f'116.87.176.34/{mask}', 0)
    print(net, len(list(net)))
    # 32768