ct=0
import ipaddress
net=ipaddress.ip_network(f'214.187.224.0/255.255.224.0', 0)
for ip in net:
    a=bin(int(ip))[2:].zfill(32)
    if a.count('1')%6!=0 and a[-4:]=='1000':
        ct+=1
print(ct)