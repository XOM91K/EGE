#s = 'У мечта все хорошо и замечательно'
s = 'горбушато'
#Методы строк
print(s.join('ПРИВЕТ'))
s = 'РЫБА'
print('%'.join(s))
s = 'ШАР'
print('##'.join(s))
print(s.replace('о', 'у', 2))
print(s.split('б'))
print(s.upper())
print(s.zfill(11))
print(s.split('о'))

# print(s.index('е'))
# print(s.rindex('е'))
# print(s.lower())
#
# print('---------------------')
# print(s.count('о')) #выводит количество символов "о"
# print(s.islower()) #True или False
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())
# print(s.istitle())
# print(s.isupper())
print(s)