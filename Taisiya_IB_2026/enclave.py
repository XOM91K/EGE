import subprocess
passes = open('/Users/zarif/ff/rockyou.txt', encoding='latin-1').readlines()
enc = open('/Users/zarif/ff/taisiya/1110/Thomas_Eckhart_10.png.enc', 'rb').read()
for x in passes:
    x = x.strip()
    out = subprocess.run(['openssl', 'enc', '-d', '-aes-256-cbc', '-k', x]
                         , input=enc, capture_output=True).stdout
    if 'PNG' in out.decode('latin-1')[:10]:
        out2 = subprocess.run(['openssl', 'enc', '-d', '-aes-256-cbc', '-k', x, '-out', 'flag2.png'], input=enc, capture_output=True)
        print(x)
        break