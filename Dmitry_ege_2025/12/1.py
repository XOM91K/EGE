s = '9' * 100
while '33333' in s or '999' in s:
    if '33333' in s:
        s = s.replace('33333', '99', 1)
    else:
        s = s.replace('999', '3', 1)
print(s)

# for x in range(100):
#     print('Нет')
# s = 'ОЛОВО'
# s.replace('О', 'А')
# print(s)
# s = '3333333333333'
# s = s.replace('333', '8', 2)
# # 83333333
# print(s)