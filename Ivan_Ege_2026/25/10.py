def isp(d):
    for i in range(2, int(d**0.5)+1):
        if d%i == 0:
            return False
    return d > 1

def dels(d):
    res = []
    for i in range(1, int(d**0.5)+1):
        if d%i == 0:
            res.append(i)
            res.append(d//i)
    return sorted(set(res))

mx = []
a = []
for i in range(3162, 7746):
    d = len(dels(i**2))
    if isp(d):
        a.append([d, i ** 2])
a = sorted(a, key=lambda d: -d[0])
for x in a:
    print(x[1], x[0])
# 43046721 17
# 24137569 7
# 47045881 7
# 25411681 5
# 28398241 5
# 38950081 5
# 47458321 5

# 43046721 17
# 24137569 7
# 47045881 7
# 12117361 5
# 13845841 5
# 20151121 5
# 25411681 5