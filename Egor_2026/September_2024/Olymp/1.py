#Zadacha1. Долгая тренировка 2023
N = int(input())
M = int(input())
S = int(input())
P = int(input())
seconds = N * (M * 60 + S) + P * (N - 1)
print(seconds // 60)
print(seconds % 60)
# mins = 0
# seconds = 0
# for i in range(N):
#     mins += M
#     seconds += S + P
# seconds -= P
# mins += seconds // 60
# seconds = seconds - (seconds // 60 * 60)
# print(mins)
# print(seconds)