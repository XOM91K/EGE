# s = [100, 200, 400, -50]
# s.append(-500)
# print(sum(s))
# print(max(s))
# print(min(s))
# print(len(s))
# print(sorted(s))
# print(sorted(s)[::-1])

# s = 'один$два$три'
# s = s.split('$')
# print(s)

s = input()
s = s.split(' ')
s = list(map(int, s))
print(sum(s))

# [50, 100]