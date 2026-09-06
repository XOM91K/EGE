import subprocess
s = open('rockyou.txt', 'rb').readlines()
#enc = open('secret_10.txt-2.enc', 'rb')
for x in s:
    x = x.strip()
    out2 = subprocess.run(['openssl', 'pkey' '-in', 'alice_private_10.pem', '-passin', f'pass:{x.decode('latin-1')}'], capture_output=True).returncode
    #out = subprocess.run(['openssl', 'pkeyutl' '-decrypt', '-inkey', 'alice_private_10.pem', '-in', 'secret_10.txt-2.enc', '-passin', f'pass:\'{x}\''], capture_output=True).stdout
    #print(out)
    # if b'vsosh' in out:
    #     print(out)
    if out2 == 1:
        print(out2)
        break
    else:
        print(x)