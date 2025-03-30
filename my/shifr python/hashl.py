import hashlib
hash_object = hashlib.sha256(b"Hello").hexdigest()
print(hash_object)
