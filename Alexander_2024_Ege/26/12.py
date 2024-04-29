l=open("12.txt")
n=400
arr=sorted([int(x) for x in l])
print(arr)
i = 0
j = len(arr) - 1
yashik = 0
mass = 0
while i < j:
    if arr[i] + arr[j] <= 400:
        yashik += 1
        i += 1
    else:
        mass += arr[j]
    j -= 1
print(yashik, mass)