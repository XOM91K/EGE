import ipaddress
for mask in range(0, 33):
    net1 = ipaddress.ip_network(f'200.154.190.12/{mask}', 0)
    net2 = ipaddress.ip_network(f'200.154.184.0/{mask}', 0)
    if net1 == net2:
        print(net1, mask)
# a = 5
# b = 7
# print('У Вани есть', a, 'яблок, а у Миши есть', b, 'бананов')
# print(f'У вани есть {a} яблок, а У Миши есть {b} бананов')