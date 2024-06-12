def return_gl_count(s):
    count_gl = 0
    for x in s:
        if x in 'АИОЕЁЯУЫаиоеёяуы':
            count_gl += 1
    return count_gl

s = input()
print(return_gl_count(s))