# В текстовом файле k7a-2.txt
# находится цепочка из символов
# латинского алфавита A, B, C, D, E, F.
# Найдите длину самой длинной (подцепочки,
#                              состоящей)
# из символов A, C, D (в произвольном порядке).
s = open('2.txt').readline()
s = s.replace('C', '@')
s = s.replace('D', '@')
s = s.replace('A', '@')
s = s.replace('F', 'E').replace('B', 'E').split('E')
print(len(max(s, key=len)))