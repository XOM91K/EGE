import ipaddress
ip = ipaddress.ip_address('68.30.20.77')
bin_ip = bin(int(ip))[2:].zfill(32)
ct = 0
for mask in range(15, 33):
    ip_net = ipaddress.ip_network(f'68.30.20.77/{mask}', 0)
    if ip in ip_net:
        ip_net_bin = bin(int(ip_net.network_address))[2:].zfill(32)
        if ip_net_bin.count('1') == 32 - mask:
            for y in ip_net:
                y = bin(int(y))[2:].zfill(32)
                if y.count('1') == 10:
                    ct += 1
print(ct)
#print(bin_ip)