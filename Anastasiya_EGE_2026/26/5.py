l = [[int(d) for d in x.split()] for x in open('5.txt')]
rating = [-1] * 996
new_l = []
for x in range(len(l)):
    new_l.append([l[x][0], x + 1, 0])
    new_l.append([l[x][1], x + 1, 1])
new_l = sorted(new_l)
nums = []
lt = 0
rt = -1
for x in new_l:
    if x[-1] == 0 and x[1] not in nums:
        rating[lt] = x[1]
        print(x[1])
        lt += 1
        nums.append(x[1])
    elif x[-1] == 1 and x[1] not in nums:
        rating[rt] = x[1]
        print(x[1])
        rt -= 1
        nums.append(x[1])

# print(new_l)
# print(rating)
# 800 120
# 150 200
# 250 300
# 60 100
# 180 220
#
# ответ: 3,  1
#
# [60] [100] [120] [150], [180], [200], [220], [250], [300], [800]
#
# 1. 60 100
# 2. 150 200
# 3. 180 220
# 4. 250 300
# 5. 800 120
# первое число - продолжительность в режиме ожидания
# второе число - продолжительность в активном