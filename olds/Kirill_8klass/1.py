def xor_decrypt(encrypted_text, key):
    answer_str = ''
    for x in encrypted_text:
        answer_str += chr(ord(x) ^ key)
    return answer_str
s1 = input()
s2 = int(input())
print(xor_decrypt(s1, s2))
