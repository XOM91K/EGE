#nums = [int(x) for x in open(r'C:\Users\Zarif\Downloads\27B_9870.txt')]
nums = [int(x) for x in open(r'1.txt')]
# K = 1440
# M = 25600
K = 144
M = 256

# Вычисляем префиксные суммы
prefix_sums = [0]
for num in nums:
    prefix_sums.append((prefix_sums[-1] + num) % 100)
print(prefix_sums)
# Массив для подсчета количества префиксных сумм с каждым остатком
remainder_counts = [0] * 100
remainder_counts[0] = 1  # Начальное значение для суммы 0

count = 0

# Проходим по всем префиксным суммам
for i in range(1, len(prefix_sums)):
    # Для текущего индекса i проверяем подпоследовательности длиной от K до M
    # Подпоследовательность допустима, если ее длина не меньше K
    if i >= K:
        # Добавляем подпоследовательности, удовлетворяющие условиям задачи
        count += remainder_counts[(prefix_sums[i] - 24) % 100]

    # Обновляем количество префиксных сумм с текущим остатком для будущих итераций
    remainder_counts[prefix_sums[i]] += 1

    # Удаляем из рассмотрения префиксные суммы, которые больше не будут участвовать в подсчете из-за ограничения по максимальной длине M
    if i > M:
        remainder_counts[prefix_sums[i - M]] -= 1

print(count)