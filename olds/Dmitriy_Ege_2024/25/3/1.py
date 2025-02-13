# Среди натуральных чисел, не превышающих 109, найдите все числа,
# соответствующие маске 20*23, которые кратны 2023, причём сумма
# цифр каждого такого числа кратна 7 и меньше 20. В ответе запишите все найденные числа в
# порядке возрастания, справа от каждого числа – частное от его деления на 2023.
import fnmatch
for x in range(2023, 10**9 + 1, 2023):
    if fnmatch.fnmatch(str(x), '20*23'):
        if sum([int(d) for d in str(x)]) % 7 == 0 and sum([int(d) for d in str(x)]) < 20:
            print(x, x // 2023)