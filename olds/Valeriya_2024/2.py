def return_list_sr(l):
    sr = sum(l) / len(l)
    return [d for d in l if d > sr]


l = [66, 55, 103, 1575, -844, 13, 44, -22, -55, -33]
print(return_list_sr(l))