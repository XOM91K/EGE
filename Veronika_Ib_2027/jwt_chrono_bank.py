import jwt
import json
print(jwt.decode(algorithms='HS256', jwt='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZ3Vlc3QiLCJyb2xlIjoidXNlciJ9.rY0LH14yMHRxi57ACrGJsk8RSJlzoq_6y35fbhxkNJg', key='secretkey'))