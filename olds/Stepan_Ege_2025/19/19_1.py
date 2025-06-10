# у соперника ходы будут через:
# or = если он ходит глупо
# and = если он ходит умно
# у нашего игрока всегда ходы будут через "OR"
def g(s, p):
    if s >= 68 and p == 2:
        return 1
    if s < 68 and p == 2:
        return 0
    if s >= 68 and p < 2:
        return 0
    if p % 2 == 0:
        return g(s + 1, p + 1) or g(s + 4, p + 1) or g(s * 5, p + 1)
    else:
        return g(s + 1, p + 1) or g(s + 4, p + 1) or g(s * 5, p + 1)
for S in range(1, 68):
    if g(S, 0):
        print(S)