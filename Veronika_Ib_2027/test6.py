import subprocess
enc = open("c5_hash.txt", "rb").read()
for w in open("c5_words.txt", 'rb'):
    w = w.strip()
    out = subprocess.run(
        ["openssl", "enc", "-d", "-aes-256-cbc", "-pbkdf2", "-k", w],
        input=enc, capture_output=True
    ).stdout
    print(out)
