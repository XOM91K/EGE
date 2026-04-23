def f(x, y, ct):
    if x in [20, 30, 40]:
        ct += 1
    if x<y: return 0
    if x==y and ct >= 2: return 1
    if x==y and ct < 2: return 0
    if x>y: return f(x-1, y, ct)+f(x-3, y, ct)+f(x//3, y, ct)
print(f(49, 12, 0))
# print(f(49,12))
# print(f(49, 40)*f(40, 30)*f(30,12))
# print(f(49, 30)*f(30, 20)*f(20,12))
# print(f(49, 40)*f(40, 20)*f(20,12))
# print(f(49, 40)*f(40, 30)*f(30,20)*f(20, 12))
# print(316540 + 317408 + 315666 + 193648)