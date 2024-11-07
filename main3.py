import re
text = open('24.txt').readline()
match = re.findall(r"[A-WZ]*X[A-WZ]*Y[A-WZ]*|[A-WZ]*Y[A-WZ]*X[A-WZ]*", text)
print(len(max(match, key=len)))

