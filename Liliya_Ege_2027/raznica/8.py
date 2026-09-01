d = list(map(int, input().split()))
if len(d) % 2 != 0:
    print(-1)
else:
    ct_chet = 0
    ct_nch = 0
    for x in d:
        if x % 2 == 0:
            ct_chet += 1
        else:
            ct_nch += 1
    print(abs(ct_chet - ct_nch) // 2)
    # 2 3 3 3 3 3   ::: 5 - 1 = 4
    # 2 3 3 3  3 - 1 = 2 // 2 = 1