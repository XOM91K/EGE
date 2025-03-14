from functools import *
# Отрезки
# (№ 4974) На числовой прямой даны два отрезка: P = [55; 80], Q = [20; 105]. Найдите наименьшую возможную длину
# отрезка A, при котором формула (x ∈ Q) → ( ((x ∈ P) ≡ (x ∈ Q)) ∨ (¬(x ∈ P) → (x ∈ A)) ) тождественно истинна, то
# есть принимает значение 1 при любых x.
def p(x): return 550 <= x <= 800
def q(x): return 200 <= x <= 1050


def f(x, a1, a2):
    return q(x) <= ((p(x) == q(x)) or ((not p(x)) <= (a1 <= x <= a2)))


m = float("inf")
for a1 in range(100, 1060):
    for a2 in range(a1 + 1, 1060):
        if all(f(x, a1, a2) == 1 for x in range (100, 1060)):
            m = min(m, a2 - a1)

print(m)