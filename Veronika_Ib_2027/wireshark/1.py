import re, base64
s = open('1.txt').read()
m = re.findall(r'part\d-([\w=]+)\.', s)
print(s)
m = [base64.b64decode(x).decode() for x in m]
print(m)
# vsosh{DNS_3xf1ltr4t10n_D3t3ct3d}