import random

challenge = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
             [5, 2, 0, 0, 0, 0, 0, 0, 0],
             [0, 8, 7, 0, 0, 0, 0, 3, 1],
             [0, 0, 3, 0, 1, 0, 0, 8, 0],
             [9, 0, 0, 8, 6, 3, 0, 0, 5],
             [0, 5, 0, 0, 9, 0, 6, 0, 0],
             [1, 3, 0, 0, 0, 0, 2, 5, 0],
             [0, 0, 0, 0, 0, 0, 0, 7, 4],
             [0, 0, 5, 2, 0, 6, 3, 0, 0]]


def local_matrix(a, b):
    a, b = (a // 3) * 3, (b // 3) * 3
    return [challenge[x][y] for x in range(a, a + 3) for y in range(b, b + 3)]


def stolb(a):
    return [challenge[x][a] for x in range(9)]


def proverk():
    return sum(row.count(0) for row in challenge)


def exit():
    for row in challenge:
        print(row)


def is_valid(num, row, col):
    if num in challenge[row]:
        return False
    if num in stolb(col):
        return False
    if num in local_matrix(row, col):
        return False
    return True


def sudook():
    empty_positions = [(i, j) for i in range(9) for j in range(9) if challenge[i][j] == 0]

    def solve():
        if not empty_positions:
            return True

        row, col = empty_positions.pop()

        for num in range(1, 10):
            if is_valid(num, row, col):
                challenge[row][col] = num

                if solve():
                    return True

                challenge[row][col] = 0

        empty_positions.append((row, col))
        return False

    if solve():
        print("Судоку решено:")
    else:
        print("Нет решения для данного судоку.")

    exit()


# Вызов функции для решения судоку
sudook()
