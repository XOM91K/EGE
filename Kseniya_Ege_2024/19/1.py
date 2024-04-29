#19
def f(a, p):
    if a>=129 and p==3:
        return False
    if a < 129 and p==3:
        return True
    if a >= 129 and p == 2:
        return True
    if a<129 and p == 2:
        return False
    if p%2==0:
        return f(a+1, p+1) or f(a*2, p+1)
    if p%2==1:
        return f(a+1, p+1) and f(a*2, p+1)
for s in range(1, 129):
    if f(s, 1)==True:
        print(s)
#20
# def f(a, p):
#     if a>=129 and p==4:
#         return True
#     if a>=129 and p==3:
#         return False
#     if a<129 and p==4:
#         return False
#     if p%2==1:
#         return f(a+1, p+1) or f(a*2, p+1)
#     if p%2==0:
#         return f(a+1, p+1) and f(a*2, p+1)
# for s in range(1, 129):
#     if f(s, 1)==True:
#         print(s)