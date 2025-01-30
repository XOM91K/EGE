# from passlib.hash import bcrypt_sha256
#
# # Генерация хэша для пароля "admin"
# password_hash = bcrypt_sha256.hash("admin")
# print(password_hash)
from werkzeug.security import generate_password_hash

# Используйте bcrypt
hash_password = generate_password_hash('admin', method='pbkdf2:sha256', salt_length=8)
print(hash_password)