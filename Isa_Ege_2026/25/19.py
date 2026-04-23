import fnmatch
import re
for x in range(10980, 10 ** 10, 10980):
    if fnmatch.fnmatch(str(x), '20[13579][13579]22[02468][02468][02468][02468][02468]'):
        print(x, x // 10980)