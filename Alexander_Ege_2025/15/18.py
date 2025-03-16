#№ 8473 (Уровень: Средний)
for A in range(1, 10000):
    can = '' #can = '10101010101010101010101011111111111111111000' => '01'
    for x in range(1, 10000):
        if (((x % 115 == 0) and (x % 5 != 0)) or (((A % x == 0) <= (A % 5 != 0)) and (not(5 <= A <= 137)))) == 1:
            can += '1'
        else:
            can += '0'
    if len(set(can)) == 2:
        print(A)
        break