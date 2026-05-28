l = [d for d in range(1, 1_000_000)]
t = (d for d in range(1, 1_000_000))
print(l.__sizeof__())
print(t.__sizeof__())
s = 'abracadabra'
