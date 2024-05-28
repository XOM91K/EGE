def kingdom_gift(*args, **kwargs):
    lst = []
    if 'letter' not in kwargs:
        kwargs['letter'] = 'a'
    for x in args:
        keys = 0
        d = 0
        if 'largest' in kwargs:
            d += 1
            if len(x) <= kwargs['largest']:
                keys += 1
        if 'count' in kwargs:
            d += 1
            if len(set(x.lower())) >= kwargs['count']:
                keys += 1
        if 'letter' in kwargs:
            d += 1
            if kwargs['letter'].lower() in x.lower():
                keys += 1
        if d == keys:
            lst.append(x)
    sorted_list = sorted(lst, key=lambda d: (len(d), reversed))[::-1]
    return sorted_list