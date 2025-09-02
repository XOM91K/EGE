s = open(r'C:\Users\Zarif\Downloads\24_66.txt').readline()
for x in range(1, 1000):
    if s.count('KOT' * x) > 0:
        print(x)