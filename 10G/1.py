s = 'Hello World!'
glas = 'eoiuya'
for x in s:
    if x in glas:
        s = s.replace(x, '*')
print(s[::-1])