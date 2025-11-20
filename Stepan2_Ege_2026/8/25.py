import itertools
k = 0
for x in itertools.product(sorted('МИНУС'), repeat=4):
    x = ''.join(x)
    #print(x)
    k += 1
    print(k, x)
    # x = x.replace('М', '#')
    # x = x.replace('И', '@')
    # x = x.replace('Н', '#')
    # x = x.replace('У', '@')
    # x = x.replace('С', '#')
    # if x.count('#') >= x.count('@'):
    #
    #     print(k, x)