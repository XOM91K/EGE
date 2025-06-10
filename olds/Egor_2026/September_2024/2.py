N, V, K = [int(x) for x in input().split()]
sm = V
kk = K
rabbit = 'YES'
for x in range(N - 1):
    if V - K > 0:
        sm += V - K
    else:
        rabbit = 'NO'
    K += kk
print(rabbit, sm)