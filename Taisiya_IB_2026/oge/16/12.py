# d = 0
# l = []
# while d!=0:
#  d = int(input())
#  if d == 0:
#   break
#  if d % 7 == 5:
#   l.append(d)
# If len(l) == 0:
#  print(«NO»)
# else:
#  print(sum(l) / len(l)
#

d = 1
l = []
while d!=0:
 d = int(input())
 if d == 0:
  break
 if d % 7 == 0 and d % 10 == 2:
  l.append(d)
print(sum(l))