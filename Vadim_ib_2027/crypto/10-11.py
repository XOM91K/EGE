# # # Генератор ключей "Конвейер-DE"
# # # Трехступенчатая система кодирования
# # # ВНИМАНИЕ: Сбой на конвейере - порядок нарушен
# #
# # def main():
# #     # Маска для финальной ступени кодирования
# #     MASK = 0x5A
# #
# #     # Эталонные поврежденные данные с конвейера
# #     ENC = [
# #         182, 178, 184, 182, 130, 91, 132, 140, 91, 138, 162, 174, 166, 38, 128, 85,
# #         164, 93, 212, 242, 188, 83, 89, 115
# #     ]
# #
# #     def rol1(x):
# #         """Поворот влево на 1 бит (Rotate Left)"""
# #         return ((x >> 1) | (x << 7)) & 0xFF
# #
# #     # Применяем трехступенчатый процесс конвейера к пользовательскому вводу
# #     encrypted_input = []
# #     for i, char in enumerate(ENC):
# #         # Этап 1: Смещение по позиции (добавляем индекс)
# #         y = rol1(char)
# #         final = ((y ^ MASK) - i) & 0xFF
# #         encrypted_input.append(final)
# #     print(encrypted_input)
# #     print(bytes(encrypted_input))
# #
# # if __name__ == "__main__":
# #     main()
# # import html
# #
# print(html.unescape('&gt'))
# # print(html.escape('asdsad'))
# # print(1)
# import html
#
#
# def render_login(username: str) -> str:
#     # БЛОК ДЛЯ РЕДАКТИРОВАНИЯ:
#     username = html.escape(username)
#     html = f"""
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
#     return html
#
#     # КОНЕЦ БЛОКА ДЛЯ РЕДАКТИРОВАНИЯ
import requests
req = requests.session()
for i in range(1000):
    get = req.get("http://proginf.ru:19001/spin")
    if i % 100 == 0:
        print(get.text)
    if "ctf" in get.text:
        print(get.text)
