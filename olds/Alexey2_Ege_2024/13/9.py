import ipaddress
for y in range(0, 256):
    try:
        for x in ipaddress.ip_network('51.50.135.169/255.255.255.' + str(y), False):
            #x = f'{x:b}'
            #x = ''.join([bin(int(d))[2:].zfill(8) for d in str(x).split('.')])
            x = sum([int(d) for d in str(x).split('.')])
            print(x)
    except:
        print('ошибка при y = ', y)