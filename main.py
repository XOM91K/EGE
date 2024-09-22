import random
l = [rnd for x in range(10) if (rnd := random.randint(5, 100)) % 2 == 0]
print(l)