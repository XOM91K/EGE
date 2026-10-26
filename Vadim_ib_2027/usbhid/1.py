import re
s = open('usbhid.txt').read()
m = re.findall(' = Usage: Keyboard ([A-Za-z0-9]+)', s)
print(''.join(m))