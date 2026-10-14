import subprocess
passes = open('/Users/zarif/ff/rockyou.txt', encoding='latin-1').readlines()
enc = open('/Users/zarif/ff/taisiya/1110/secret_9.txt.enc', 'rb').read()
for x in passes:
    x = x.strip()
    out = subprocess.run(['openssl', 'enc', '-d', '-aes-256-cbc', '-k', x]
                         , input=enc, capture_output=True).stdout
    if 'vsosh' in out.decode('latin-1'):
        print(out.decode())