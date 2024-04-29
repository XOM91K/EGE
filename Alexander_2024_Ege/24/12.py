l = open('12.txt').readline().strip()
l=l.split("O")
mx = 0
for i in l:
    if i.count('F') <=2:
        print(i)
        mx = max(mx, len(i)+2)
print(mx)