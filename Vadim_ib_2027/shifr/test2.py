
def xor_dynamic_key(text, initial_key):
    a = []
    first = chr(ord(text[0]) ^ initial_key)
    a.append(first)
    for i in range(1, len(list(text))):
        first = chr(ord(text[i]) ^ ord(a[-1]))
        a.append(first)

    return "".join(a)
a1 = input()
b1 = int(input())
print(xor_dynamic_key(a1, b1))