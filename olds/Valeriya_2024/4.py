def return_str_len(s):
    return list(filter(lambda d: len(d) % 2 != 0, s))


s = ['Дождь', 'Снег', 'Метель', 'Мороз', 'Мёд', 'Картошка']
print(return_str_len(s))
