import re
s = open(r'C:\Users\Zarif\Downloads\154_1 (2).txt').readline()
m = re.findall(r'(?:WXYZ|XYZ|YZ|Z)?(?:VWXYZ)+(?:VWXY|VWX|VW|V)?', s)
print(len(max(m, key=len)))
#    VWXYZVWXYZVWXYZVWXYZVWXYZVWXYZVWXYZ
#XYZ VWXYZVWXYZVWXYZVWXYZVWXYZVWXYZVWXYZ V