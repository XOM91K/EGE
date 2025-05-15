import string
stt =string.ascii_uppercase
print(stt[:24])
for x in '0123456789'+stt[:24]:
    s1 = int('GP45'+x+'234',34)
    s2 = int('P7'+x+'34',34)
    s3 = int(x+'AI9834', 34)
    if (s1+s2*s3)%13==0:
        print(x, (s1+s2*s3)//13)