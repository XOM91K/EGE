s = open(r'C:\Users\Zarif\Downloads\24 (25).txt').readline()
s = s.split('E')
mn = 10 ** 10
#240 "Е" в строке (минимальная длина строки)
for i in range(len(s) - 238):
    ln = 0
    for j in range(239):
        ln += len(s[i + j])
    mn = min(mn, ln + 240)
print(mn)