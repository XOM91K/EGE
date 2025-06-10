import random
d = ['Петя', 'Ваня', 'Оля', 'Олег', 'Гриша', 'Ира', 'Егор', 'Зариф', 'Марина', 'Наташа']
ct = 0
for x in range(3):
    rc = random.choice(d)
    if len(rc) > 5:
        print(rc, 'Имя длинное')
    else:
        print(rc, 'Имя короткое')
        continue
    print('Поздравляем ваше имя длинное! Это круто!')
    ct += 1
print(ct)