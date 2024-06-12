def g(s, p):
    if (p ==2 or p ==4 ) and s >= 435:
        return 1
    elif p == 4 and s < 435:
        return 0
    elif p < 4 and s >= 435:
        return 0
    # and - умные ходы (любые ходы)
    # or - глупые ходы (неудачные ходы)
    # наш игрок ВСЕГДА ХОДИТ "OR"
    if p % 2 == 0:
        return g(s + 5, p + 1) and g(s * 3, p + 1)
    else:
        return g(s + 5, p + 1) or g(s * 3, p + 1)
for x in range(1, 434):
    if g(x, 0):
        print(x)