def count_valid_R(R_min, R_max):
    def count_cases(a, b):
        # Вычисляет количество N, для которых R = b * N + a попадает в [R_min, R_max]
        N_min = (R_min - a + b - 1) // b  # округление вверх
        N_max = (R_max - a) // b          # округление вниз
        if N_min > N_max:
            return 0
        return N_max - N_min + 1

    # Случай 1: R = 2N
    count_2N = count_cases(0, 2)

    # Случай 2: R = 2N + 1
    count_2N_plus1 = count_cases(1, 2)

    # Случай 3: R = 4N + 2
    count_4N_plus2 = count_cases(2, 4)

    # Случай 4: R = 4N + 3
    count_4N_plus3 = count_cases(3, 4)

    # Суммируем все случаи
    total = count_2N + count_2N_plus1 + count_4N_plus2 + count_4N_plus3
    return total

# Заданные границы
R_min = 1_100_000_000
R_max = 1_987_653_210

# Вычисление количества доступных R
total_available_R = count_valid_R(R_min, R_max)
print(f"Количество доступных чисел R в диапазоне [{R_min}; {R_max}]: {total_available_R}")
