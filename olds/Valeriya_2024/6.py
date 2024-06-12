def get_str_len_sorted(s):
    return sorted(s, key=len)[::-1]


s = ['Дождь', 'Снег', 'Метель', 'Мороз', 'Мёд', 'Картошка']
print(get_str_len_sorted(s))