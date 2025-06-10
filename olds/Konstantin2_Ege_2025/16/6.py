import sys #1-й этап попытки
import functools #2-й этап попытки
sys.setrecursionlimit(15000) #1-й этап попытки
@functools.lru_cache(None) #2-й этап попытки
def F(n):
    if n == 0:
        return 1
    if n > 0:
        return 2 * F(1-n) + 3 * F(n-1) + 2
    if n < 0:
        return -F((-n))
for x in range(1, 15000): #3-й этап
    F(x) #3-й этап
print(sum(map(int, str(F(14750)))))
# print(F(14750).count('1') + F(14750).count('2')*2 + F(14750).count('3')*3 + F(14750).count('4')*4 + F(14750).count('5')*5 +\
#       F(14750).count('6')*6 + F(14750).count('7')*7 + F(14750).count('8')* + F(14750).count('9')*9)