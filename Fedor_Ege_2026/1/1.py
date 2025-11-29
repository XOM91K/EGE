from itertools import *
t = '13 15 17 23 24 31 32 34 36 37 42 43 46 51 57 63 64 67 71 73 75 76'
g = 'аб ав ад ба бв вб ва вд вг ве гв ге гк да дв де ед ев ег ек ке кг'
for per in permutations('абвгдек'):
    new_g = t
    for i in range(1, 8):
        new_g = new_g.replace(str(i), per[i-1])
    if set(g.split()) == set(new_g.split()):
        print('1 2 3 4 5 6 7')
        print(*per)