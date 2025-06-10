import ipaddress
ct = 0
for mask in range(0, 33):
    net = ipaddress.ip_network(f'208.207.224.0/{mask}', 0)
    ip = ipaddress.ip_address('208.207.230.65')
    if ip in net:
        ct += 1
print(ct)