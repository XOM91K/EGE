def f(x,y, ct):
    if x == 20 or x == 30 or x == 40:
        ct += 1
    if x < y:
        return 0
    if x == y and ct >= 2:
        return 1
    if x == y and ct < 2:
        return 0
    return f(x-1,y, ct)+f(x-3,y, ct)+f(x//3,y, ct)
print(f(49, 12, 0))
# v1 = ((f(49,40)*f(40,30)*f(30,12)))
# v2 = (f(49,40)*f(40,20)*f(20,12))
# v3 = (f(49,30)*f(30,20)*f(20,12))
# v4 = (f(49,40)*f(40,30)*f(30,20)*f(20,12))
# print(122892+122018+123760+v4)
# print(v1) # 122892
# print(v2) # 122018
# print(v3) # 123760
# print(v4)