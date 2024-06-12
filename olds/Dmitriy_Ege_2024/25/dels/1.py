#
# Напишите программу, которая ищет среди целых чисел,
# принадлежащих числовому отрезку [100806; 100950], числа,
# имеющие ровно 6 различных делителей. Выведите для каждого найденного числа два
# наибольших делителя, не равных самому числу, в порядке возрастания.

import time
start_time = time.time()  # время начала выполнения
def dels(n):
    l = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            l.append(x)
            l.append(n // x)
    return sorted(set(l))
for x in range(10080600, 10095100):
    if len(dels(x)) == 6:
        print(dels(x)[-3], dels(x)[-2])
end_time = time.time()  # время окончания выполнения
execution_time = end_time - start_time  # вычисляем время выполнения
print(f"Время выполнения программы: {execution_time} секунд")