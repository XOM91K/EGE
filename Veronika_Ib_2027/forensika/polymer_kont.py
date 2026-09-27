import base64
s = 'dUtboY<qSvcr;&TI5l5#GkJD2a9?zGFnBO$FmPWpeE'
alf = sorted('qwertyuiopasdfghjklzxcvbnm')
s = base64.b85decode(s).decode()
for x in range(len(s)):
    if s[x] in alf:
        print(alf[alf.index(s[x]) -4], end='')
    else:
        print(s[x],end='')