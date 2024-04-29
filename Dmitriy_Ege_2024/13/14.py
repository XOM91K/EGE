import ipaddress
for A in range(0, 256):
    ip_count = 0
    ip_all_count = 0
    try:
        for x in ipaddress.ip_network('108.8.190.123/255.255.' + str(A) + '.0', False):
            ip_all_count += 1
            x = f'{x:b}'
            if x[:16].count('1') <= x[16:].count('1'):
                ip_count += 1
        if ip_count == ip_all_count:
            print(A)
    except:
        pass