for i in range(251, 300):
    x = i * '5'
    while '55555' in x:
        x = x.replace('55555', '88', 1)
        x = x.replace('888', '555', 1)
    print(i, x.count('5'))