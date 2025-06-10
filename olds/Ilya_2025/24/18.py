s = open(r'C:\Users\Zarif\Downloads\24_17641.txt').readline()
s = s.replace('**', '$').replace('++', '$')
s = s.replace('*+', '$').replace('+*', '$')
s = s.split('$')
print(s)
mx_len = 0
for x in s:
    for y in range(len(x)):
        a = ''
        for z in range(y, len(x)):
            a += x[z]
            try:
                if eval(a) == 0:
                    mx_len = max(len(a), mx_len)
            except:
                pass
print(mx_len)