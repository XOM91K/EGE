#Реализуйте собственный калькулятор,
# который принимает выражение, записанное
# в обратной польской нотации. Требуется
# поддержать операции +, -, *. Все числа во
# входной последовательности положительны и меньше 10.
d = input()
s = []
for x in d:
    if x == '+':
        a = int(s.pop())
        b = int(s.pop())
        s.append(a + b)
    elif x == '-':
        a = int(s.pop())
        b = int(s.pop())
        s.append(b - a)
    elif x == '*':
        a = int(s.pop())
        b = int(s.pop())
        s.append(a * b)
    else:
        s.append(x)
print(s[0])
