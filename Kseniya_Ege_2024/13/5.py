from ipaddress import *
# for a in range(0, 256):
#     ip=ip_address(f'154.127.{a}.230')
#     m=ip_address('255.255.255.192')
#     s=ip_network(f'{ip}/{m}',0)
#     s=ip_address(s)
#     s=f'{s:b}'
#
#     s1=s[:8]
#     s2=s[-8:]
#     if s1.count('1')>s2.count('1'):
#         print(a)

for A in range(0, 256):
    can = True
    for x in ip_network(f'154.127.{A}.230/255.255.255.192', False):
        x = f'{x:b}'
        if x[:16].count('1') <= x[-16:].count('1'):
            can = False
            break
    if can:
        print(A)