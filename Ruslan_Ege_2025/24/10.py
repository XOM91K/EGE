import re, string
# print(string.ascii_uppercase)
s = open(r'C:\Users\Zarif\Downloads\329_1 (5).txt').readline()
# m = re.findall(r'A?B?C?D?E?F?G?H?I?J?K?L?M?N?O?P?Q?R?S?T?U?V?W?X?Y?Z?', s)
# print(max(m, key=len))
for y in range(26, 1, -1):
    for x in range(0, len(s) - y):
        if len(set(s[x: x + y])) == y:
            print(y, len(set(s[x: x + y])), set(s[x: x + y]), s[x: x + y])
            exit()