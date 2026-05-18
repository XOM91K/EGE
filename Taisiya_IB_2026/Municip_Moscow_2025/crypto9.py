import random
import base64
XOR_KEY = random.randint(0, 255)
# R0kyREFJQlNHUTJTQU1SVEdNUURFTkJWRUFaREdPQkFHSTJUR0lCU0dNNFNBTVJSRzRRREVNWlVFQVlUUU1SQUdJMkRBSUJSSEFZU0FNUlJHNFFERU1SWkVBWkRJTkJBR0kyVEtJQlNHUTNDQU1SVUdJUURDT0JTRUFaRENOWkFHSTJERUlCU0dNNENBTUpZR01RREVNWlNFQVpERU5KQUdFM1RTSUJTR1VZUT09PT0=
flag = "R0kyREFJQlNHUTJTQU1SVEdNUURFTkJWRUFaREdPQkFHSTJUR0lCU0dNNFNBTVJSRzRRREVNWlVFQVlUUU1SQUdJMkRBSUJSSEFZU0FNUlJHNFFERU1SWkVBWkRJTkJBR0kyVEtJQlNHUTNDQU1SVUdJUURDT0JTRUFaRENOWkFHSTJERUlCU0dNNENBTUpZR01RREVNWlNFQVpERU5KQUdFM1RTSUJTR1VZUT09PT0="
encrypted_flag = base64.b64decode(flag.encode("utf-8")).decode("utf-8")
encrypted_flag = base64.b32decode(encrypted_flag.encode("utf-8")).decode("utf-8")
#encrypted_flag = " ".join(map(str, encrypted_flag))
# encrypted_flag = []
# for c in flag:
#     encrypted_flag.append(ord(c) ^ XOR_KEY)
XOR_KEY = 134
encrypted_flag = encrypted_flag.split()
flag = []
for c in encrypted_flag:
    flag.append(chr(int(c) ^ XOR_KEY))
print(''.join(flag))