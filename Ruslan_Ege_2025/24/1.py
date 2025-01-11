import re
s = open(r'C:\Users\Zarif\Downloads\153_1.txt').readline()
match = re.findall(r"(?:NPO|PNO)+", s)
print(max(match, key=len))
print(len(max(match, key=len)))
# s = ['Никита', 'Тимофей', 'Яна', 'Ли']
# print(len(max(s, key=len)))