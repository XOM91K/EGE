import random

challenge = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
             [5, 2, 0, 0, 0, 0, 0, 0, 0],
             [0, 8, 7, 0, 0, 0, 0, 3, 1],
             [0, 0, 3, 0, 1, 0, 0, 8, 0],
             [9, 0, 0, 8, 6, 3, 0, 0, 5],
             [0, 5, 0, 0, 9, 0, 6, 0, 0],
             [1, 3, 0, 0, 0, 0, 2, 5, 0],
             [0, 0, 0, 0, 0, 0, 0, 7, 4],
             [0, 0, 5, 2, 0, 6, 3, 0, 0]]

challenge1 = challenge

def local_matrix(a, b):
    a, b = (a // 3) * 3, (b // 3) * 3
    return [challenge[a][b], challenge[a][b + 1], challenge[a][b + 2],
            challenge[a + 1][b], challenge[a + 1][b + 1], challenge[a + 1][b + 2],
            challenge[a + 2][b], challenge[a + 2][b + 1], challenge[a + 2][b + 2]]

def stolb(a):
    l = []
    for x in range(9):
        l.append(challenge[x][a])
    return l

def proverk():
    ct = 0
    for x in range(9):
        ct += challenge[x].count(0)
    return ct

def exit():
    for x in range(9):
        print(challenge[x])


# for i in range(9):
#     for j in range(9):
#         if challenge[i][j] == 0:
#             try:
#                 challenge[i][j] = random.choice(
#                     list({1, 2, 3, 4, 5, 6, 7, 8, 9} - set(challenge[i] + stolb(j) + local_matrix(i, j))))
#             except:
#                 continue
def sudook():
    for i in range(9):
        for j in range(9):
            if challenge[i][j] ==0:
                try:
                    challenge[i][j] =random.choice(list({1,2,3,4,5,6,7,8,9}-set(challenge[i]+stolb(j)+local_matrix(i,j))))
                except:
                    continue
        # if proverk()>=1:
        #     challenge=challenge1
        #     sudook()
        # else:
        #     exit()
sudook()

exit()



    # [
    #     [3, 1, 6, 5, 7, 8, 4, 9, 2],
    #     [5, 2, 9, 1, 3, 4, 7, 6, 8],
    #     [4, 8, 7, 6, 2, 9, 5, 3, 1],
    #     [2, 6, 3, 4, 1, 5, 9, 8, 7],
    #     [9, 7, 4, 8, 6, 3, 1, 2, 5],
    #     [8, 5, 1, 7, 9, 2, 6, 4, 3],
    #     [1, 3, 8, 9, 4, 7, 2, 5, 6],
    #     [6, 9, 2, 3, 5, 1, 8, 7, 4],
    #     [7, 4, 5, 2, 8, 6, 3, 1, 9]