# Задача о ПСП (Правильной скобочной последовательности
s = input()
stack = []
for i in range(len(s)):
    if s[i] == '(' or s[i] == '[' or s[i] == '{':
        stack.append(s[i])
    else:
        if s[i] == ')' and stack[-1] == '(':
            stack.pop()
        elif s[i] == ']' and stack[-1] == '[':
            stack.pop()
        elif s[i] == '}' and stack[-1] == '{':
            stack.pop()
        else:
            print('NO')
            break
else:
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')