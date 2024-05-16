ct=0
d=2*729**2014+2*243**2016-2*81**2018+2*27**2020-2*9**2022-2024
def v27(n):
    s=[]
    while n>0:
        s.append(n % 27)
        n//=27
    return s[::-1]
ct = 0
for x in v27(d):
    if x > 9:
        ct += 1
print(ct)