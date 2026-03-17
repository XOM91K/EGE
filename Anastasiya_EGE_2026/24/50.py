import tqdm
s = open('50.txt').readline()
for x in '0123456789':
    s = s.replace(x, '#')
s = s.split('#')
mx = []
for x in s:
    if x != '':
        if len(set(x)) == 26:
            mx.append(len(x))
print(max(mx))