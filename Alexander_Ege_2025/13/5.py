#https://examinf.ru/tasks/308
import ipaddress
for mask in range(16, 33):
    ip1 = ipaddress.ip_network('211.188.211.49/' + str(mask), 0)
    ip2 = ipaddress.ip_network(f'211.188.200.115/{mask}', 0)
    if ip1 == ip2:
        k = 0
        for ip in ip1:
            ip = bin(int(ip))[2:].zfill(32)
            if ip.count('1') % 2 != 0:
                k += 1
        print(k)