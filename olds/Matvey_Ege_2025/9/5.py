l = [([int(d) for d in x.split()]) for x in open('5.txt')]
k = 0
for x in l:
   if x[0] != max(x) and x[0] != min(x) and x[-1] != max(x) and x[-1] != min(x):
       if (sorted(x)[2] - sorted(x)[1]) > 0:
           if (max(x) - min(x)) % (sorted(x)[2] - sorted(x)[1]) == 0:
               k+=1
print(k)