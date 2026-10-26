import re
s = open('flagusb.txt').read()
m = re.findall(r' = Usage: Keyboard ([\w{}]+)', s)
print(''.join(m))
# vsosh{usb_k3y_str0k3s_4re_r3ally_f4n}