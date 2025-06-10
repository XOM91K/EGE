import ipaddress
ct=0
for x in list(ipaddress.ip_network('111.194.0.0/255.254.0.0',0))[1:-1]:
    l = str(x).split('.')
    l2=''
    for i in l:
        l2+=bin(int(i))[2:].zfill(8)
    if (l2.count('1')-l2.count('0'))%2==0:
        ct+=1
print(ct)