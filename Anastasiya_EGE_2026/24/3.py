s = open(r'C:\Users\Zarif\Downloads\24_314.txt').readline()
s = s.replace('OCK', '#')
s = s.replace('ST#', '@')
print(s.count('#'))