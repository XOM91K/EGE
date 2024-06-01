#Тернарный условный оператор
age = int(input())
print('Вы подросток' if age < 18 else 'Вы взрослый')
print('Вы подросток' if age < 18 else 'Вы взрослый' if 18 <= age <= 65 else 'Вы пожилой')
# age = 25
# if age < 18:
#     print('Вы подросток')
# elif 18 <= age <= 65:
#     print('Вы взрослый')
# else:
#     print('Вы пожилой')
