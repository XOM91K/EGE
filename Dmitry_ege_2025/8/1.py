import itertools
for x in itertools.permutations('НОЖИ', 4):
    x = ''.join(x)
    print(x)

# 2 2! = 1 * 2 => 2
# 3 3! = 1 * 2 * 3 => 6
# 4 4! = 1 * 2 * 3 * 4 =  24