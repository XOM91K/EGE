import re
s = open(r"C:\Users\Zarif\Downloads\24_629_1 (2).txt").readline()
# Определите максимальное количество
# идущих подряд символов, среди которых не более трёх точек.
m = re.findall(r"\w*\.\w*\.\w*\.\w*", s)
print(len(max(m, key=len)))