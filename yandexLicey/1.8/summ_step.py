def sum_of_powers(n):
    total_sum = 0
    for i in range(1, n + 1):
        power_sum = sum(range(1, i + 1, 2))
        total_sum += pow(i, power_sum)
    return total_sum


print(sum_of_powers(int(input())) + 2)
