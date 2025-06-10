s = open(r'C:\Users\Zarif\Downloads\1397_2 (2).txt').readline()
s = s.split('RSQ')
minn = 10**10
for i in range(len(s) - 129):
    ln = 0
    for y in s[i + 129]:
        if y == 'Q':
            ln += 1
        else:
            ln += 1
            break
    else:
        ln += 1
    minn = min(minn, len(''.join(s[i:i+129])) + 3 * 130 + ln)

    # if minn> len(''.join(a[i:i+131])):
    #     minn = len(''.join(a[i:i+131]))
    #     s = ''.join(a[i:i+131])
print(minn)

# import re
# a = open('24.txt').readline()
# m = re.findall(r'(RSQ\w*)?(\w*RSQ\w*){130}\w*[^Q]+', a)
# otv = max(m, key = len)
# print(otv, len(otv))