ct=0
import ipaddress
net=ipaddress.ip_network('111.194.0.0/255.254.0.0', 0)
for ip in net.hosts():
    a=bin(int(ip))[2:].zfill(32)
    if (abs(a.count('1')-a.count('0')))%2==0:
        ct+=1
print(ct)