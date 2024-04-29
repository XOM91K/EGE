# import ipaddress
# ct = 0
# for x in ipaddress.ip_network('105.224.200.224/255.255.255.224', False):
#     x = bin(int(x))[2:]
#     print(x)
#     #x = ''.join([bin(int(d))[2:] for d in str(x).split('.')])
#     if x.count('1') % 4 == 0:
#         ct += 1
# print(ct)
d = 1231
def tr(d):
    s = ''
    while d > 0:
        s += str(d % 3)
        d //= 3
    s = s[::-1]
    return s