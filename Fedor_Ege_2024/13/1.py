import ipaddress
for A in range(0, 256):
    for x in ipaddress.ip_network(f'248.112.{A}.35/255.255.255.240', False):
        print(x)
        x = f'{x:b}'
        print(x)
        if x[:16].count('0') > x[-16:].count('0'):
            break
    else:
        print(A)