for A in range(0, 10, 2):
    for B in range(1000):
        if '0' not in str(B) and '2' not in str(B) and '4' not in str(B) and '6' not in str(B) and '8' not in str(B):
            s = int('1' + str(A) + '2157' + str(B) + '4')
            if s % 133 == 0:
                print(s, s // 133)