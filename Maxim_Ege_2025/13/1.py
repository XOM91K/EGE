import ipaddress
for x in ipaddress.ip_network('250.135.101.80/255.255.255.248', False):
    x = f'{x:b}'
    # x = x.split('.')
    # x[0] = bin(int(x[0]))[2:].zfill(8)
    # x[1] = bin(int(x[1]))[2:].zfill(8)
    # x[2] = bin(int(x[2]))[2:].zfill(8)
    # x[3] = bin(int(x[3]))[2:].zfill(8)
    # x = ''.join(x)
    if x.count('0') % 3 == 0:
        print(x)
# a = 5
# b = 6
# print('У Вани есть', a, 'груш, а у Ромы есть ', b, 'яблок.')
# print(f'У Вани есть {a} груш, а у Ромы есть  {b} яблок.') #format-строка f-строка