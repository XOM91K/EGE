import fnmatch
for x in range(2627, 10 ** 9, 2627):
    if fnmatch.fnmatch(str(x), '7*53?3*1'):
        print(x, x // 2627, sum(map(int, str(x))))
#75323971 37
#715313711 29
#753536561 41
#775393201 37
#785323261 37