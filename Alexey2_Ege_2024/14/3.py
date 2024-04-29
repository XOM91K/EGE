for x in '0123456789abcd':
    if (int(x + 'b09', 17) + int(x + '8E8', 15)) % 155 == 0:
        print((int(x + 'b09', 17) + int(x + '8E8', 15)) // 155)
