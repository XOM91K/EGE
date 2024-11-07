import itertools

fours = float('inf')  # Начальное значение для поиска минимума

for n in range(30):
    for y in itertools.product('12', repeat=n):
        if y.count('1') == y.count('2'):
            y = ''.join(y)
            B = "0" + y + "0"

            while "00" not in B:
                if "011" in B:
                    B = B.replace("011", "101", 1)
                elif "01" in B:
                    B = B.replace("01", "40", 1)
                elif "02" in B:
                    B = B.replace("02", "20", 1)
                elif "0222" in B:
                    B = B.replace("0222", "1401", 1)

            ones = B.count("1")
            twos = B.count("2")
            if ones == 8 and twos == 13:
                fours = min(fours, B.count('4'))

print(fours if fours != float('inf') else 0)
