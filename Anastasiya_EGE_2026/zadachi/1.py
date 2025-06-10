user_input = input()
user_input = user_input.replace(' ', '')
user_input = user_input.lower()
print(user_input)
if user_input == user_input[::-1]:
    print(True)
else:
    print(False)