nch = '13579'
ch = '02468'
for x in range(7777, 10**9, 7777):
    if len(str(x)) == 9 and str(x)[0] in ch and str(x)[1] in nch and str(x)[2] in ch and str(x)[3] in ch and str(x)[4] in nch and str(x)[5] in ch and str(x)[6] in nch and str(x)[7] == '7' and str(x)[8] == '7':
        print(x, x // 7777)