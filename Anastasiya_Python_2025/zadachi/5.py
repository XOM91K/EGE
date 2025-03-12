# Ввод данных
strings = input().split()
#далее ваш код...
strings = sorted(strings, key=len)
print(strings)
# s = ['Николай', 'Ян', 'Артем']
# print(max(s, key=len))