import ipaddress
d = []
for x in ipaddress.ip_network('135.221.128.0/255.255.128.0', 0):
    x = bin(int(x))[2:].zfill(32)
    d.append(x.count('1'))
print(min(d))
#print(bin(22))
# a = 5
# b = 9
# print('У нас есть', a, 'яблок', 'а у них есть', b, 'бананов')
# print(f'У нас есть {a} яблок а у них есть {b} бананов')
s = 'ПРИВЕТКАКДЕЛА'
print(s.zfill(20))