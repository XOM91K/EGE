# # import requests
# # s = requests.session()
# # for x in range(1000):
# #     get = s.get('http://proginf.ru:19001/spin').text
# #     if 'ctf' in get:
# #         print(get)
# #     if x % 100 == 0:
# #         print(x)
# import html
#
# def render_login(username: str) -> str:
#     # БЛОК ДЛЯ РЕДАКТИРОВАНИЯ:
#     username = html.escape(username)
#     html1 = f"""
#     <html>
#       <head><title>Minecraft License Login</title></head>
#       <body>
#         <h1>Welcome, {username}!</h1>
#         <form method="post" action="/do_login">
#           <input name="username" value="{username}">
#           <input type="password" name="password">
#           <button>Login</button>
#         </form>
#       </body>
#     </html>
#     """
#     return html1
# print(render_login('qwe'))
#
#     # КОНЕЦ БЛОКА ДЛЯ РЕДАКТИРОВАНИЯ
from urllib.parse import urlparse
def is_safe_url(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.scheme == 'http' and parsed.hostname == 'public' and parsed.port == 5067:
        return True
    else:
        return False
    #  ^z ^~ ^} ^u    ^q ^{ ^~ ^z ^p  ^t ^{      ^u ^t ^p ^z   ^x   ^~ ^r ^p ^} ^x