import jwt
creditionals = {
    'user': 'admin',
    'role': 'admin'
}
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZ3Vlc3QiLCJyb2xlIjoidXNlciJ9.rY0LH14yMHRxi57ACrGJsk8RSJlzoq_6y35fbhxkNJg"
print(jwt.decode(token, key="secretkey", algorithms='HS256'))
print(jwt.encode(creditionals, key="secretkey", algorithm='HS256'))