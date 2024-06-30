# import requests
#
# base_url = "https://stimul.sch1576.ru/api/achievements/"
# cookie = "SESSION=cb722631be83ccd2d38152b9fa98cf83%2F7f272c5281da63eed53be5ed545da26c3b9db61e2b172f9d665955af618bac4445428a67fd5e93022a8c8a35512fadd3e19daa231e8b91671dabd9fe89f8fca0"
#
# for userid in range(200, 500):
#     for ach_id in range(136, 220):
#         url = f"{base_url}{ach_id}?userId={userid}"
#         headers = {"Cookie": cookie}
#
#         response = requests.get(url, headers=headers)
#
#         if response.status_code == 200:
#             print(f"User ID: {userid}, Achievement ID: {ach_id}")
#             data = response.json()
#
#             user_value = data["data"]["points"]
#             user_points = data["data"]
#
#             print("userValue:", user_value)
#             #print("userPoints:", user_points)
#         else:
#             print("Ошибка при получении данных")