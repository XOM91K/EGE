import ipaddress
for mask in range(15,33):
    net=ipaddress.ip_network(f'75.32.145.15/{mask}',0)
    ip = ipaddress.ip_address('75.32.136.235')
    if ip in net:
        print(mask)
# 19 => 13 нулей
# 2 ^ 13 = 8192
# 4095