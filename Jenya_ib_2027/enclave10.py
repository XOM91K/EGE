import subprocess
wl = open('/Users/zarif/ff/rockyou.txt', encoding='latin-1').readlines()
fl = open('Thomas_Eckhart_10.png.enc', 'rb').read()
print(fl[:10])
for pas in wl:
    pas = pas.strip()
    out = subprocess.run(['openssl', 'enc', '-d', '-aes-256-cbc', '-k', pas], input=fl, capture_output=True).stdout
    if 'PNG' in out[:20].decode('latin-1'):
        print(out[:20].decode('latin-1'), pas)