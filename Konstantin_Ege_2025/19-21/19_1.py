# Ваня делает ходы, при нечётных p
# Петя делает ходы, при чётных p
# Ваня когда походил, он делает чётные p
# Петя когда походил, он делает нечётные p
def g(s, p):
    if s >= 58 and p == 2:
        return 1
    elif s < 58 and p == 2:
        return 0
    elif s >= 58 and p < 2:
        return 0
    if p % 2 == 0:
        return g(s + 4, p + 1) and g(s + 1, p + 1) and g(s * 2, p + 1)
    else:
        return g(s + 4, p + 1) or g(s + 1, p + 1) or g(s * 2, p + 1)
