s = open('20.txt').readline().split('AHAHA')
print(len(max(s, key=len)) + 6)