import ipaddress
for mask in range(0, 33):
    net = ipaddress.ip_network(f'92.52.42.0/{mask}', 0)
    ip = ipaddress.ip_address('92.52.42.52')
    if ip in net:
        print(net.netmask)



#f-строка

# a = 9
# b = 4
# print('У Леши есть', a, 'яблок, а у Лизы есть', b, 'банана')
# print(f'У Леши есть {a} яблок, а у Лизы есть {b} банана')