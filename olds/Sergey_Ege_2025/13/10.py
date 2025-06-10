import ipaddress

ct = 0
for x in ipaddress.ip_network("111.194.0.0/255.254.0.0",False).hosts():
  x = bin(int(x))[2:].zfill(32)
  if (x.count("0") - x.count("1")) % 2== 0:
    ct +=1
print(ct)