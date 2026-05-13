import tqdm
s=open(r'C:\Users\Zarif\Downloads\24_26078 (1).txt').readline()
m=1000
for l in tqdm.tqdm(range(len(s))):
    for r in range(l + 529, len(s)):
        c=s[l:r+1]
        if c.count('W')>90:
            break
        elif c.count('W')==90 and c.count('2025')>=110:
             m=min(m, len(c))
print(m)