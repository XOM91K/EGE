import ipaddress
for A in range(0, 256):
    can = True
    try:
        for x in ipaddress.ip_network('243.46.4.198/255.255.' + str(A) + '.0', False):
            x = f'{x:b}'
            if not(x[:16].count('0') <= x[16:].count('0')):
                can = False
        if can == True:
            print(A)
    except:
        None