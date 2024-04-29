for x in '0123456789abcdefgh':
    c1 = int('973F8' + x + '24', 18)
    c2 = int('7241' + x + '1E5', 18)
    c3 = int('31' + x + '154C', 18)
    if (c1 + c2 + c3) % 11 == 0:
        print((c1 + c2 + c3) // 11)