for x in range(1001, 1, -1): # 0
    for y in range(1001 - x): # 1
        for z in range(1001 - x - y): # 2
            if x + y + z == 1000 and y == 2 * z and (x * 2 + z) - (y + z * 2) == 1640:
                print(x)
# for i in range(1, 1000):
#     for j in range(1, 1000 - i):
#         k0= j
#         k1= i
#         k2= 1000 - k0 - k1
#         st = k0*'0'+k1*'1'+k2*'2'
#         if len(st)==1000:
#             smn=sum([int(x) for x in st])
#             st =st.replace('0', '*')
#             st = st.replace('1', '@')
#             st = st.replace('2', '1')
#             st = st.replace('@', '0')
#             st = st.replace('*', '2')
#             smk = sum([int(x) for x in st])
#             #print(smn, smk, abs(smn-smk), k0)
#             if abs(smn-smk)==1640 and st.count('0')==k2*2:
#                 print(k0, k1, k2)
#         else:
#             break