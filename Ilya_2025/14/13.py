import string
stt = string.ascii_uppercase[:15]
for x in '0123456789'+stt:
    s1 = int('11353'+x+'12',25)
    s2 = int('135'+x+'21',25)
    if (s1 +s2)%24==0:
        print((s1+s2),(s1+s2)//24)