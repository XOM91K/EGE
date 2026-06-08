# def g(n,m):
#     if n<=1 and m==2:
#         return 1
#     elif n>1 and m==2:
#         return 0
#     elif n<=1 and m<2:
#         return 0
#     if m%2==0 and n>=4 and n%3==0:
#         return g(n-1,m+1) and g(n-4,m+1)and g(n//3,m+1)
#     elif m%2==0 and n<4 and n%3==0:
#         return g(n-1,m+1) and g(n//3,m+1)
#     elif m%2==0 and n>=4 and n%3!=0:
#         return g(n-1,m+1) and g(n-4,m+1)
#     elif m%2==0 and n<4 and n%3!=0:
#         return g(n-1,m+1)
#
#     elif m%2!=0 and n>=4 and n%3==0:
#         return g(n - 1, m + 1) or g(n - 4, m + 1) or g(n // 3, m + 1)
#     elif m % 2 != 0 and n < 4 and n % 3 == 0:
#         return g(n - 1, m + 1) or g(n // 3, m + 1)
#     elif m % 2 != 0 and n >= 4 and n % 3 != 0:
#         return g(n - 1, m + 1) or g(n - 4, m + 1)
#     elif m % 2 != 0 and n < 4 and n % 3 != 0:
#         return g(n - 1, m + 1)
# for S in range(4,101):
#     if g(S,0):
#         print(S)
# def g(n, m):
#     if n <= 1 and m == 3:
#         return 1
#     elif n > 1 and m == 3:
#         return 0
#     elif n <= 1 and m < 3:
#         return 0
#     if m % 2 != 0:
#         if n >= 4 and n % 3 == 0:
#             return g(n - 1, m + 1) and g(n - 4, m + 1) and g(n // 3, m + 1)
#         elif n < 4 and n % 3 == 0:
#             return g(n - 1, m + 1) and g(n // 3, m + 1)
#         elif n >= 4 and n % 3 != 0:
#             return g(n - 1, m + 1) and g(n - 4, m + 1)
#         elif n < 4 and n % 3 != 0:
#             return g(n - 1, m + 1)
#     else:
#         if n >= 4 and n % 3 == 0:
#             return g(n - 1, m + 1) or g(n - 4, m + 1) or g(n // 3, m + 1)
#         elif n < 4 and n % 3 == 0:
#             return g(n - 1, m + 1) or g(n // 3, m + 1)
#         elif n >= 4 and n % 3 != 0:
#             return g(n - 1, m + 1) or g(n - 4, m + 1)
#         elif n < 4 and n % 3 != 0:
#             return g(n - 1, m + 1)
#
#
# for S in range(4, 101):
#     if g(S, 0):
#         print(S)

def g(n, m):
    if n <= 1 and (m == 2 or m == 4):
        return 1
    elif n > 1 and m == 4:
        return 0
    elif n <= 1 and m < 4:
        return 0
    if m % 2 == 0:
        if n >= 4 and n % 3 == 0:
            return g(n - 1, m + 1) and g(n - 4, m + 1) and g(n // 3, m + 1)
        elif n < 4 and n % 3 == 0:
            return g(n - 1, m + 1) and g(n // 3, m + 1)
        elif n >= 4 and n % 3 != 0:
            return g(n - 1, m + 1) and g(n - 4, m + 1)
        elif n < 4 and n % 3 != 0:
            return g(n - 1, m + 1)
    else:
        if n >= 4 and n % 3 == 0:
            return g(n - 1, m + 1) or g(n - 4, m + 1) or g(n // 3, m + 1)
        elif n < 4 and n % 3 == 0:
            return g(n - 1, m + 1) or g(n // 3, m + 1)
        elif n >= 4 and n % 3 != 0:
            return g(n - 1, m + 1) or g(n - 4, m + 1)
        elif n < 4 and n % 3 != 0:
            return g(n - 1, m + 1)


for S in range(4, 101):
    if g(S, 0):
        print(S)
