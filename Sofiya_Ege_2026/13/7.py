import ipaddress
ct = 0
for mask in range(0, 33):
    net=ipaddress.ip_network(f'192.214.116.184/{mask}', 0)
    if bin(int(net.network_address))[2:].count('1') % 5 == 0 and bin(int(net.network_address))[2:].count('1') > 0:
        print(mask)
        ct += 1
print(ct)