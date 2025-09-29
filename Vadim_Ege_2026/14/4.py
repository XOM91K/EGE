import base64,requests
i = input("URL (http://tasks.ctfd.infosec.moscow:20021/): ")
i2 = ""
print(i)
wd = requests.Session()
for a in range(102):
 r1 = wd.get(i).text
 if "base32" in r1:
  i2 = "base32"
 else:
  i2 = 'base64'
 print(r1)
 r = r1.split("'")[1]
 print(r,r1)
 if i2 == 'base32':
  f = str(base64.b32encode(r.encode()))[2:-1]
 else:
  f = str(base64.b64encode(r.encode()))[2:-1]
 print(wd.get(i+"?answer="+f).text,f)