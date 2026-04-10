for x in range(1, 10001):
    try:
        s = open(f'{x}.txt', encoding='utf-8').read()
        if 'flag' in s:
            print(s[s.find('flag'):s.find('flag')+20])
    except:

        pass
# ['ab', 'bc']