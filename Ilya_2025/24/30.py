s = open(r'C:\Users\Zarif\Downloads\826_1 (2).txt').readline()
m = re.findall(r"A", s)
print(len(max(m, key=len)))