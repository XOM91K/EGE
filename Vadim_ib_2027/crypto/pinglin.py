from os import system
import subprocess
s = open('secret_9.txt.enc', 'rb').read()
d = open('rockyou.txt', encoding='latin-1').readlines()
for x in d:
    x = x.strip()
    #out = system(f'openssl enc -d -aes-256-cbc -in secret_9.txt.enc -k {x}')
    out = subprocess.run(['openssl', 'enc', '-d', '-aes-256-cbc', '-k', x], input=s, capture_output=True)
    # if out.:
    #     print(x)
    #     break
    if b'vsosh' in out.stdout:
        print(out.stdout)
    #print(out.stdout)