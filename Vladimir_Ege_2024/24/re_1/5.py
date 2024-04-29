import re
s = 'утконос, нос, носовой платок, Носков'
t = re.findall(r'[нН]ос', s)
print(t)