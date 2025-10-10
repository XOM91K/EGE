# list
import random
days = []
for x in range(1000000):
    days.append(random.randint(-10, 30))

sr = sum(days) / len(days)

print(days)
print(sr)
# import random
# day1 = random.randint(-10, 30)
# day2 = random.randint(-10, 30)
# day3 = random.randint(-10, 30)
# day4 = random.randint(-10, 30)
# day5 = random.randint(-10, 30)
# day6 = random.randint(-10, 30)
# day7 = random.randint(-10, 30)
#
# sr = (day1 + day2 + day3 + day4 + day5 + day6 + day7) / 7
# print(sr)