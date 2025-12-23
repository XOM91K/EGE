d = int(input())
pobeditel_min = 100
pobeditel_sec = 0
for x in range(d):
    mn = int(input())
    sec = int(input())
    if mn * 60 + sec < pobeditel_min * 60 + pobeditel_sec:
        pobeditel_min = mn
        pobeditel_sec = sec
print(pobeditel_min, pobeditel_sec)