for x in range(7777,10**9,7777):
    m = str(x)
    if len(m) == 9:
        if int(m[0])%2==0 and int(m[1])%2!=0 and int(m[2])%2==0 and int(m[3])%2==0 and int(m[4])%2!=0 and int(m[5])%2==0 and int(m[6])%2!=0 and int(m[-1])==7 and int(m[-2])==7:
            print(x,x//7777)
