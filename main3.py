def reverse_duga(s, l, r):
    n = len(s)
    if l <= r:
        return s[:l-1] + s[l-1:r][::-1] + s[r:]
    else:
        return s[:r - 1] + s[l - 1] + s[r:l - 1] + s[r - 1] + s[l + 1:]

# Пример использования функции
initial_string = "purest"
operations = [(3, 2), (1, 1)]

for l, r in operations:
    initial_string = reverse_duga(initial_string, l, r)

print(initial_string)  # Вывод: oscar