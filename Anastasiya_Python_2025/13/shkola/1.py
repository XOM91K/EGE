import ipaddress
for mask in range(0, 33):
    net = ipaddress.ip_network(f'111.91.192.0/{mask}', 0)
    ip = ipaddress.ip_address('111.91.200.28')
    if ip in net:
        print(mask)
# a = 5
# b = 7
# print('У Вити есть', a, 'яблок, а у Гриши есть', b, 'бананов')
# print(f'У Вити есть {a} яблок, а у гриши есть {b} бананов') # f-строка
