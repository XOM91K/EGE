import itertools
st = set()
def f(x, y, z, w):
    return (not((not(x<=(not w))) and z)) and (not(w<=z)) and (x<=(not z))
for i in itertools.product([0,1], repeat=5):
    t=[(1, 0, i[0], 0),
       (1, 0, i[1], i[2]),
       (i[3], 1, i[4], 1)]
    if len(set(t))==3:
        for j in itertools.permutations('xyzw'):
            if [f(**dict(zip(j, r)))for r in t]==[1, 0, 0]:
                st.add(j)
print(len(st))

# #s=[' ', '1', '0', '1', ' ']
# # вправо +1
# # влево -1
# # остаться на месте 0
# # остановиться 2
# '''prog={
#     (' ', 0): (' ', -1, 1),
#     (' ', 2): (' ', 2, 1),
#     ('0', 1): ('1', -1, 1),
#     ('1', 1): ('0', -1, 1)
# }
# def mt(s):
#     s = list(' '+s+' ')
#     q=0
#     i=-1
#     while True:
#       cmd=prog[(s[i], q)]
#       s[i] = cmd[0]
#       if cmd[1]==2:
#         break
#       i+=cmd[1]
#       q=cmd[2]
#     return ''.join(s)
# res=mt(f'{375:b}')
# print(int(mt(res,2)))'''
#
# prog={
#     (' ', 0):(' ', 2),
# }
# def mt(s):
#     s = list(' '+s+' ')
#     q=0
#     i=-1
#     while True:
#       cmd=prog[(s[i], q)]
#       s[i] = cmd[0]
#       if cmd[1]==2:
#         break
#       i+=cmd[1]
#       q=cmd[2]
#     return ''.join(s)