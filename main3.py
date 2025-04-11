import string
def caesar(st: str, x: int):
    alfu = string.ascii_uppercase
    alfl = string.ascii_lowercase
    decoded_str = ''
    for s in st:
        if s.islower():
            decoded_str += alfl[(x + alfl.index(s)) % len(alfl)]
        else:
            decoded_str += alfu[(x + alfu.index(s)) % len(alfu)]
    return decoded_str
#local_64 = "PQaRXRZxgMYuRTGovoaovWzHkppiyjqnnMKbppFhNtXulZNJNCWgCaEdvbaqrbnPyvcKtgVYcEjsyAIUjltCRsQMwdCdoLRjvQCZMwEEtBxJjzTgHwzgiTxHBkLGTcywdaAGDLbVDLMiQuDnonRvADntFZjasIVAfuERfgBiHlzxTiSDMayrIWNJRxXBItlAgaoWiXsJeZvICXtcSkEQRzbBvzpWyMVunDcYkTvQdFWLHqIiOXJHBAuCXSpynxmlqVibuiGwTBxMclMyNpysxMzvRfngyfwmAkbIUVcJtbDCCByptaK"
local_64 = "oyXEqEPRcScXCSwYtHKM"
alfu1 = string.ascii_uppercase
alfl1 = string.ascii_lowercase
print(alfl1)
print(alfu1)
for y in [4, -4]:
    print(caesar(local_64, y))
