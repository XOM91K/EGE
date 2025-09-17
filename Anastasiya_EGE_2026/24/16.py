import re
s = open(r'C:\Users\Zarif\Downloads\24-261.txt').readline()
s = s.replace('EA', '##')
s = s.replace('NPC', '###')
print(s)
# m = re.findall(r'(?:EA|NPC)+', s)
# print(len(max(m, key=len)))
#
print(len('#######################################################################################################################################'))