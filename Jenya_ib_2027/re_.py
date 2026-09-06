import re
#s = open('test.txt')
s = 'asdiusdgvsoshsavsoshidg89201202020asdasvs123osh{diwdgqwiudgqwdiwqdgquid}d1298316293asdad89004000050asjkdasdg'
m = re.findall(r'vs\d+osh{.+}', s)
print(m)