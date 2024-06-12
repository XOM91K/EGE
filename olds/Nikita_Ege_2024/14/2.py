a = (19**81) + (23**709) - 4
otv = 0
ch = ""
while a > 0:
    ch = (str(a%9)) + ch
    a = a // 9
for i in range(len(ch)-1):
    if (ch[i] == "8" and ch[i+1] != "8" and ch[i + 1] != '0'):
        otv += 1
print(otv)