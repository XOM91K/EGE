import ipaddress
for A in range(0, 256):
    flag = True
    for x in ipaddress.ip_network('196.233.' + str(A) + '.52/255.255.255.248', False):
        x = f'{x:b}'
        left = x[:16]
        right = x[16:]
        if left.count('1') <= right.count('1'):
            flag = False
    if flag == True:
        print(A)
