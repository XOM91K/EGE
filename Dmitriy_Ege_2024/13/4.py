import ipaddress
for x in range(0, 255):
    try:
        ip1 = ipaddress.IPv4Network(f'51.50.135.169/255.255.255.{x}', False)
        ip1 = str(ip1)[:-3].split('.')
        if int(ip1[0]) + int(ip1[1]) + int(ip1[2]) + int(ip1[3]) == 404:
            print(x, ip1)
    except:
        print('словил ошибку')
