s = open(r'C:\Users\Zarif\Downloads\24var09-12 (1).txt').readline()
s = s.replace('2', '1').split('11')
print(s)
print(max(s, key=len), len(max(s, key=len)))