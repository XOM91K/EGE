import itertools
ct = 0
for x in itertools.permutations('ВЕБИНАР', 7):
    x = ''.join(x)
    x = x.replace('В', '#')
    x = x.replace('Б', '#')
    x = x.replace('Н', '#')
    x = x.replace('Р', '#')
    x = x.replace('Е', '@')
    x = x.replace('И', '@')
    x = x.replace('А', '@')
    if '##' not in x and '@@' not in x:
        ct += 1
print(ct)


nums = [1, 2, 3, 4]
print(nums[1:3] + nums[:1])