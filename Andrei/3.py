s = input()
a = input()
n = {}
s = s.split(',')
a = a.split(',')
n[s[0]] = a[0]
n[s[1]] = a[1]
n[s[2]] = a[2]
print(s)
print(a)
print(n)
# Добавьте в словарь новую пару
# "country": "Russia".
n['country'] = "Russia"
print(n)