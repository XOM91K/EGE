def is_tr(n, m, k):
    return max(n, m, k) < (sum([n,m,k]) - max(n, m, k) - min(n, m, k)) + min(n, m, k)
for A in range(1, 1000):
    for x in range(1, 1000):
        if ((not(((is_tr(x, 11, 18) == (not(max(x, 5)) > 68))))) and (is_tr(x, A,5))) == 0:
            break
    else:
        print(A)