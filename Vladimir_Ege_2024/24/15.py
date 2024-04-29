import fnmatch
s = [x.strip() for x in open('15.txt')]
st = set()
for x in s:
    if fnmatch.fnmatch(x, '195.2*.?*.14'):
        st.add(x)
print(len(st))