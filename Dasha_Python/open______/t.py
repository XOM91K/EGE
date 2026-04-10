s = open('t.txt', 'a+', encoding='utf-8')
s.write('Привет!')
s.seek(0)
print(s.read())