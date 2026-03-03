s = open('23.txt').readline()

s = s.replace('()', '#', 10000)
print(s.rindex('#') + 10000)