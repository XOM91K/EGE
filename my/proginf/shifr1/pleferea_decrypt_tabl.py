import re
import random
import math
from collections import defaultdict

# -------------------------
# Настройки/утилиты
# -------------------------

RUS_UPPER = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
EXTRA_FILL = list("0123456789.,;:!?")  # добивка, если не хватает до N*N

def only_letters(s: str):
    """Оставляем только русские буквы в верхнем регистре (включая Ё)."""
    return re.findall(r"[А-ЯЁ]", s.upper())

def prepare_plain_bigrams(letters, filler="Х"):
    """
    Разбиваем на биграммы с вставкой разделителя при повторах в паре.
    Если итог нечётной длины — добиваем filler.
    """
    res = []
    i = 0
    while i < len(letters):
        a = letters[i]
        if i + 1 == len(letters):
            b = filler
            i += 1
        else:
            b = letters[i + 1]
            if a == b:
                # вставляем filler между одинаковыми
                b = filler
                i += 1
            else:
                i += 2
        res.append((a, b))
    if len(res[-1]) != 2:
        res[-1] = (res[-1][0], filler)
    return res

def playfair_encrypt_pair(pos, N, a, b):
    """
    Шифрует пару (a,b) в соответствии с таблицей pos: {char: (r,c)}, размер N.
    Возвращает (c,d).
    """
    ra, ca = pos[a]
    rb, cb = pos[b]
    if ra == rb:
        # одна строка: сдвиг вправо
        return grid_char_at(pos, N, ra, (ca + 1) % N), grid_char_at(pos, N, rb, (cb + 1) % N)
    elif ca == cb:
        # один столбец: сдвиг вниз
        return grid_char_at(pos, N, (ra + 1) % N, ca), grid_char_at(pos, N, (rb + 1) % N, cb)
    else:
        # прямоугольник
        return grid_char_at(pos, N, ra, cb), grid_char_at(pos, N, rb, ca)

def grid_char_at(pos, N, r, c):
    # обратный поиск символа по координатам
    # (для скорости можно хранить обратный индекс отдельно)
    for ch, (rr, cc) in pos.items():
        if rr == r and cc == c:
            return ch
    raise RuntimeError("grid_char_at: inconsistent pos")

def key_to_pos(key, N):
    """Массив key длиной N*N в координаты pos: {char: (r,c)}"""
    pos = {}
    k = 0
    for r in range(N):
        for c in range(N):
            pos[key[k]] = (r, c)
            k += 1
    return pos

def score_key(key, N, pairs):
    """
    Оценка: сколько биграмм (a,b)->(c,d) объясняются таблицей.
    pairs — список кортежей (a,b,c,d).
    """
    pos = key_to_pos(key, N)
    ok = 0
    for a, b, c, d in pairs:
        ec, ed = playfair_encrypt_pair(pos, N, a, b)
        if ec == c and ed == d:
            ok += 1
    return ok

# Предварительная индексация: какие пары зависят от какой буквы
def letter_to_pairs_index(pairs):
    idx = defaultdict(list)
    for i, (a, b, c, d) in enumerate(pairs):
        idx[a].append(i); idx[b].append(i); idx[c].append(i); idx[d].append(i)
    return idx

def delta_score_for_swap(key, N, pairs, idx_by_letter, i, j, current_score):
    """
    Быстрый перерасчёт изменения счёта при обмене key[i] <-> key[j].
    Пересчитываем только пары, в которых участвуют эти буквы.
    """
    a = key[i]
    b = key[j]
    touched = set(idx_by_letter[a] + idx_by_letter[b])  # индексы пар, где участвует a или b

    # Текущая позиционная карта
    pos = key_to_pos(key, N)

    # Счёт до
    before = 0
    for k in touched:
        aa, bb, cc, dd = pairs[k]
        ec, ed = playfair_encrypt_pair(pos, N, aa, bb)
        if ec == cc and ed == dd:
            before += 1

    # Применим swap к pos
    ra, ca = pos[a]
    rb, cb = pos[b]
    pos[a], pos[b] = (rb, cb), (ra, ca)

    after = 0
    for k in touched:
        aa, bb, cc, dd = pairs[k]
        ec, ed = playfair_encrypt_pair(pos, N, aa, bb)
        if ec == cc and ed == dd:
            after += 1

    return current_score - before + after, after - before


def anneal(pairs, alphabet, N, seed=0, iters=200000, restarts=5, init_key=None):
    random.seed(seed)
    letters_used = list(alphabet)

    # добьём до N*N
    pool = [ch for ch in RUS_UPPER if ch not in letters_used] + [ch for ch in EXTRA_FILL if ch not in letters_used]
    while len(letters_used) < N * N and pool:
        letters_used.append(pool.pop(0))
    # если всё ещё меньше — добиваем искусственными Юникод-символами
    extra_code = 0x2000
    while len(letters_used) < N * N:
        letters_used.append(chr(extra_code))
        extra_code += 1

    best_key = None
    best_score = -1

    idx_by_letter = letter_to_pairs_index(pairs)

    for r in range(restarts):
        if init_key and r == 0:
            key = init_key[:]
        else:
            key = letters_used[:]
            random.shuffle(key)

        current_score = score_key(key, N, pairs)
        if current_score > best_score:
            best_key, best_score = key[:], current_score

        T0 = max(1.0, len(pairs) / 10.0)  # базовая температура
        T = T0
        cooling = 0.9995

        for it in range(iters):
            i, j = random.randrange(N * N), random.randrange(N * N)
            if i == j:
                continue

            new_score, ds = delta_score_for_swap(key, N, pairs, idx_by_letter, i, j, current_score)

            # Жадно или по Метрополису
            if ds >= 0 or random.random() < math.exp(ds / max(1e-9, T)):
                key[i], key[j] = key[j], key[i]
                current_score = new_score
                if current_score > best_score:
                    best_key, best_score = key[:], current_score

            T *= cooling

            # ранний выход, если нашли идеальное объяснение
            if best_score == len(pairs):
                break

        # print(f"Restart {r+1}/{restarts}: best_score={best_score}/{len(pairs)}")
        if best_score == len(pairs):
            break

    return best_key, best_score


def build_pairs_from_texts(plain_text, cipher_text, filler="Х"):
    p_letters = only_letters(plain_text)
    c_letters = only_letters(cipher_text)

    # Готовим биграммы открытого текста
    p_bigrams = prepare_plain_bigrams(p_letters, filler=filler)

    # Длина букв шифртекста должна соответствовать количеству биграмм * 2
    need = len(p_bigrams) * 2
    if len(c_letters) < need:
        # обрежем биграммы до доступной длины шифртекста
        cut = len(c_letters) // 2
        p_bigrams = p_bigrams[:cut]
    elif len(c_letters) > need:
        c_letters = c_letters[:need]

    # Собираем пары (a,b)->(c,d)
    pairs = []
    k = 0
    for a, b in p_bigrams:
        c, d = c_letters[k], c_letters[k + 1]
        k += 2
        # На всякий случай: если кто-то шифровал без разделителя для равных,
        # можно пропускать такие пары (но мы уже вставили filler).
        pairs.append((a, b, c, d))
    return pairs


def guess_grid_size(alphabet):
    # 5x5 или 6x6
    need = len(alphabet)
    if need <= 25:
        return 5
    elif need <= 36:
        return 6
    else:
        # вряд ли, но подстрахуемся
        n = math.ceil(math.sqrt(need))
        return n


def recover_playfair_key(plain_text, cipher_text, fillers=("Х", "Ъ"), seeds=(0, 1, 2), iters=150000, restarts=5):
    best = None
    for filler in fillers:
        pairs = build_pairs_from_texts(plain_text, cipher_text, filler=filler)
        # Алфавит — объединение букв из пар
        alphabet = set()
        for a, b, c, d in pairs:
            alphabet.update([a, b, c, d])
        N = guess_grid_size(alphabet)

