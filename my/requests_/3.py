import urllib.parse, base64
# print(urllib.)
text = rb']ArR[UnP\pnAbkqqU~Bb{r'
for y in text:
    print(chr(56 ^ y), end ='')
print()
print(base64.b64decode('eyJjcmVhdHVyZSI6ImFzZCJ9'))
print(base64.b64encode(b'{"creature":"sorceress"}'))
r = []
for x in base64.b64encode(b'{"creature":"sorceress"}'):
    r.append(x ^ 56)
print(bytes(r).decode('iso-8859-1'))
print(urllib.parse.quote(b']ArR[UnP\pnAbkqqVvN[UvT[UnB[Ar'))