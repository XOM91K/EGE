def get_palyndrom(s):
    for x in range(len(s)):
        if s[x] != s[-x - 1]:
            return False
    return True


s = '112211'
print(get_palyndrom(s))