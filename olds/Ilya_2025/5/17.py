print(int(bin(1_111_111_110)[2:-5], 2))
print(int(bin(1_444_444_416)[2:-5], 2))
N = 45138887
R = bin(N)[2:]
R += bin(N % 3)[2:].zfill(2)
R += bin(N % 5)[2:].zfill(3)
R = int(R, 2)
print(R)

# s = '123'
# print(s.zfill(10))
#34722223
#45138887
#45138887 - 34722223