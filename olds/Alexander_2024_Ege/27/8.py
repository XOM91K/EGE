l = [int(x) for x in open('8.txt')]
mx_sm = 0
k = 10000
left_mx = 0
sr_sum = 0
right_sum = 0
for i in range(len(l) - 2 * k):
    left_mx = max(left_mx, l[i])
    sr_sum = max(sr_sum, left_mx + l[i + k])
    right_sum = max(right_sum, sr_sum + l[i + 2 * k])
print(right_sum)