# def f(s,p):
#     if s < 32 and p == 2:
#         return 1
#     if s < 32 and p == 1:
#         return 0
#     if s >= 32 and p == 2:
#         return 0
#     if p%2==0:
#         if s%4==0:
#             return f(s-3,p+1) and f(s-2,p+1) and f(s//4,p+1)
#         else:
#             return f(s-3,p+1) and f(s-2,p+1)
#     else:
#         if s%4==0:
#             return f(s-3,p+1) or f(s-2,p+1) or f(s//4,p+1)
#         else:
#             return f(s-3,p+1) or f(s-2,p+1)
# for x in range(100,33,-1):
#     if f(x,0) == 1:
#         print(x)
#         break
# def f(s,p):
#     if s < 32 and p == 3:
#         return 1
#     if s >= 32 and p == 3:
#         return 0
#     if s < 32 and p < 3:
#         return 0
#     if p%2!=0:
#         if s%4==0:
#             return f(s-3,p+1) and f(s-2,p+1) and f(s//4,p+1)
#         else:
#             return f(s-3,p+1) and f(s-2,p+1)
#     else:
#         if s%4==0:
#             return f(s-3,p+1) or f(s-2,p+1) or f(s//4,p+1)
#         else:
#             return f(s-3,p+1) or f(s-2,p+1)
# for x in range(32, 500):
#     if f(x,0) == 1:
#         print(x)

def f(s, p):
    if s < 32 and (p == 2 or p == 4):
        return 1
    if s >= 32 and p == 4:
        return 0
    if s < 32 and p < 4:
        return 0
    if p % 2 == 0:
        if s % 4 == 0:
            return f(s - 3, p + 1) and f(s - 2, p + 1) and f(s // 4, p + 1)
        else:
            return f(s - 3, p + 1) and f(s - 2, p + 1)
    else:
        if s % 4 == 0:
            return f(s - 3, p + 1) or f(s - 2, p + 1) or f(s // 4, p + 1)
        else:
            return f(s - 3, p + 1) or f(s - 2, p + 1)


for x in range(32, 500):
    if f(x, 0) == 1:
        print(x)
