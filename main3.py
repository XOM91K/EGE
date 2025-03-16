def titled_str(s):
    s = [x.title() for x in s if len(x) <= 5]
    return s

print(titled_str(['про', 'доп', 'Зуб']))