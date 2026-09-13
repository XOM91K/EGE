import subprocess

rockyou = open("rockyou.txt", encoding="latin-1").readlines()
fileasinput = open("zapiska.txt.enc", "rb").read()
rock = []

for i in rockyou:
    i = i.strip()
    out = subprocess.run(['openssl', 'enc', '-d', '-md', 'md5', '-aes-256-cbc', '-k', i], input=fileasinput, capture_output=True)
    if b"ctfinf" in out.stdout:
        print(out.stdout.decode())
        break