import string
s = open('17.txt').readline()
print(len(s))
for x in range(26, -1, -1):
    for z in range(0, len(s) - (x + 1)):
        if len(set(s[z:z+x])) == len(s[z:z + x]):
            print(x)
            exit()