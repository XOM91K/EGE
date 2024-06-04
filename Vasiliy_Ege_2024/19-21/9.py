def g(s, p):
    if p == 2 and s >= 55 and s <= 77:
        return 1
    elif p == 2 and not(s >= 55 and s <= 77):
        return 0
    elif p < 2 and s >= 55 and s <= 77:
        return 0
    # and - умные ходы (любые ходы)
    # or - глупые ходы (неудачные ходы)
    # наш игрок ВСЕГДА ХОДИТ "OR"
    if p % 2 == 0:
        return g(s + 3, p + 1) and g(s * 3, p + 1) and g(s * 2, p + 1)
    else:
        return g(s + 3, p + 1) or g(s * 3, p + 1) or g(s * 2, p + 1)
for x in range(1, 54):
    if g(x, 0):
        print(x)