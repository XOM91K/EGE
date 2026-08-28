# import hashlib
# print(hashlib.pbkdf2_hmac('sha256', 'secret'.encode(), b'asd', 1000, 32).hex())
# import subprocess
#
# enc = open(r"C:\Users\Zarif\Downloads\c4_secret.enc", "rb").read()
# for w in open("wordlist.txt"):
#     w = w.strip()
#     out = subprocess.run(["openssl", "enc", "-d", "-aes-256-cbc", "-pbkdf2", "-k", w], input=enc, capture_output=True).stdout
#     if out.startswith(b"vsosh{"):
#         print("пароль:", w)
#         print(out.decode())
#         break
import subprocess
s = open('/home/kali/Desktop/secret_9.txt.enc').read()
psws = open('/usr/share/wordlists/rockyou.txt').readlines()
for psw in psws:
    psw = psw.strip()
    out = subprocess.run(['openssl', 'enc', '-d', '-aes-256-cbc', '-pbkdf2', '-k', psw], input=s, capture_output=True)
    print(out)
