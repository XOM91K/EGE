for N in range(1, 10000):
    R = bin(N)[2:] #bin - перевод  в двоичную
    R += str(R.count('1') % 2) #count - считает кол-во значений
    R += str(R.count('1') % 2) # % - деление по остатку
    if int(R, 2) > 43: #int(r,2) - перевод в 10-ую из 2-ую
        print(int(R, 2))
