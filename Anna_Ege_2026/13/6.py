import ipaddress
ct = 0
for x in ipaddress.ip_network('139.75.100.0/255.255.252.0', 0):
    x = str(x).split('.')
    if any([x[-1] == str(2 ** d - 1) for d in range(1, 9)]):
    #if x[-1] == '1' or x[-1] == '3' or x[-1] == '7'
        print(x)
        ct += 1
print(ct)
n = 101014
#if n % 2 == 0 and n % 4 == 0 and n % 8 == 0:
# if all([n % 2 == 0, n % 4 == 0, n % 8 == 0]):
#     print('Yes')
# else:
#     print('No')