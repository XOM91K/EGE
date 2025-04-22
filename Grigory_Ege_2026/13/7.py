a=[]
import  ipaddress
for x in ipaddress.ip_network('135.221.128.0/255.255.128.0',0):
    x=bin(int(x)).zfill(32)
    x = x.count('1')
    a.append(x)
print(min(a))