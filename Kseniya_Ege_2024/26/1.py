l = sorted([[int(d) for d in x.split()] for x in open('1.txt')])
ct_pr = 0
sm_pr = 0
last_client_uydet = 0
for x in l:
    if x[0] - last_client_uydet > 1:
        sm_pr += ((x[0] - 1 - last_client_uydet) + 1)
        ct_pr += 1
    last_client_uydet = x[1]
print(ct_pr + 1, sm_pr + (1439 - last_client_uydet - 1))