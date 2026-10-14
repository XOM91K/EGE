import subprocess
wl = open('/Users/zarif/ff/rockyou.txt', encoding='latin-1').readlines()
fl = open('secret_9.txt.enc', 'rb').read()
print(fl[:10])
for pas in wl:
    pas = pas.strip()
    out = subprocess.run(['openssl', 'enc', '-d', '-aes-256-cbc', '-k', pas], input=fl, capture_output=True).stdout
    if 'vsosh' in out.decode('latin-1'):
        print(out.decode('latin-1'), pas)