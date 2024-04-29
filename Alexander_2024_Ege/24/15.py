s = open(r'C:\Users\Zarif\Downloads\24_11636.txt').readline().split('A')
pr = 1
ct = 0
sm = 0
for x in s:
    ct += 1
    if len(x) == 0:
        sm += ct - 1
    else:
        sm += ct
print(sm)
#4143037975216724
#42587173055
#42587756750