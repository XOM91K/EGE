s = open(r'C:\Users\Zarif\Downloads\2_24.txt').readline()
s = s.replace('KLMN', '#')
for x in range(1, 1000):
    if '#' * x in s:
        print(x)
    else:
        break
s = 'KLMN' * 45
print(s)
#180