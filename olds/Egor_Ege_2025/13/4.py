cnt = 0
import ipaddress
l = [1, 3, 7, 15, 31, 63, 127, 255]
for x in ipaddress.ip_network("139.75.100.0/255.255.252.0", False):
    x = str(x).split('.')
    print(x)
    if int(x[3]) in l:
        cnt += 1
print(cnt)