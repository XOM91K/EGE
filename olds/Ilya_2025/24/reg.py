import re
s = 'Привет как дела у меня все хорошо три четыре раз два'
m = re.findall(r"\b\w{3}\b", s)
print(m)