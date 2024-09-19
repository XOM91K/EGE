import ipaddress
ct = 0
print(type('192.168.1.0'))
print(type(ipaddress.ip_address('192.168.1.0')))
# for x in ipaddress.ip_network('211.46.0.0/255.255.128.0', False):
#     x = bin(int(x))[2:].zfill(32)
#     if x.count('1') % 4 == 0:
#         if x[-2:] == '11':
#             ct += 1
# print(ct)