# # # # # import base64,requests
# # # # # for a in range(100):
# # # # #  c = {"session":"eyJjbnQiOjAsImxhc3RfdGFzayI6IkRPQVNDSEFZUl9FTU4ifQ.aMaAxA.iOqWg2W8p5wH9ScvRB_H55p9va4"}
# # # # #  r1 = requests.get("http://tasks.ctfd.infosec.moscow:20128/", cookies=c).text
# # # # #  print(r1)
# # # # #  r = r1.split("'")[1]
# # # # #  print(r,r1)
# # # # #  f = str(base64.b64encode(r.encode()))[2:-1]
# # # # #  print(requests.post("http://tasks.ctfd.infosec.moscow:20128/?answer="+f, cookies=c).text,f)
# # # # def xor_decrypt(data, key):
# # # #  """Расшифровка данных с помощью XOR с заданным ключом"""
# # # #  return bytes([b ^ key for b in data])
# # # #
# # # #
# # # # def is_printable(text):
# # # #  """Проверяет, состоит ли текст только из печатных ASCII символов"""
# # # #  return all(32 <= byte <= 126 or byte in [9, 10, 13] for byte in text)
# # # #
# # # #
# # # # def main():
# # # #  # Читаем зашифрованный файл
# # # #  with open('flag.enc', 'rb') as f:
# # # #   encrypted_data = f.read()
# # # #
# # # #  print(f"Размер зашифрованных данных: {len(encrypted_data)} байт")
# # # #  print(f"Первые 20 байт: {encrypted_data[:20]}")
# # # #
# # # #  # Пробуем все возможные ключи (0-255)
# # # #  possible_flags = []
# # # #
# # # #  for key in range(256):
# # # #   decrypted = xor_decrypt(encrypted_data, key)
# # # #
# # # #   # Проверяем, похоже ли это на текстовый флаг
# # # #   if is_printable(decrypted):
# # # #    try:
# # # #     decoded_text = decrypted.decode('utf-8')
# # # #     # Ищем типичные форматы флагов
# # # #     if any(flag_marker in decoded_text for flag_marker in ['flag{', 'CTF{', 'FLAG{']):
# # # #      print(f"🎉 ВОЗМОЖНЫЙ ФЛАГ с ключом {key}: {decoded_text}")
# # # #      possible_flags.append((key, decoded_text))
# # # #     elif len(decoded_text) > 10:  # Просто покажем все читаемые результаты
# # #
# # #
# # # import re
# # #
# # # s = r"""
# # # ФГІЎ          яя  д   Жh‡Ў z   z   E  z   @µїАЁ ¦ђ 5 fв%рЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x76Жh	§ g   g   E  g   @µТАЁ ™Ћ 5 SкгЖПЃ       kp8lcn50net   kp8lcn50net      < sjGxWtbWa5cK9yAlpA98Жhл« m   m   E  m   @µМАЁ iт 5 YW)kЃ       1n498kgcuhgcom   1n498kgcuhgcom      < 1cXh3XwLOIZ6gj6RWSrXЖhяЇ z   z   E  z   @µїАЁ `" 5 fхЂNЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x73Жh ґ k   k   E  k   @µОАЁ c` 5 WЏИЃ       h9wphv3kk40ru   h9wphv3kk40ru      < y6dVXeQzF5DcNutbV62RЖhё c   c   E  c   @µЦАЁ r 5 OтґpЃ       nlke9bnet   nlke9bnet      < 9l9wdJG8Lk1WswpL7fBUЖh@ј z   z   E  z   @µїАЁ ¶Щ 5 fќ –XЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x6fЖh<А k   k   E  k   @µОАЁ ЩВ 5 WYєДЕЃ   
# # # nk36m94p3qorg   
# # # nk36m94p3qorg      < edCDfIhnwz9Dw8u7DnmuЖhЧД e   e   E  e   @µФАЁ yя 5 QЙгvНЃ       a4ni6foorg   a4ni6foorg      < XixEhsk1iC42lt02beA7ЖhвИ z   z   E  z   @µїАЁ —< 5 fёT™ФЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x73ЖhН o   o   E  o   @µКАЁ яO 5 [@ис;Ѓ       zh61em0x7g07net   zh61em0x7g07net      < AKb10nQsvoBUC5X9XxfQЖhjС c   c   E  c   @µЦАЁ <Љ 5 OzЕXїЃ       hvtcn1nru   hvtcn1nru      < PJPJOXWXxL6XvafdHyqWЖhOХ z   z   E  z   @µїАЁ у; 5 fОт(2Ѓ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x68Жh@Щ i   i   E  i   @µРАЁ ys 5 UљУЕаЃ       	ausoecf9yxyz   	ausoecf9yxyz      < dCf6LItvtQarsqLcXkBhЖhdЭ z   z   E  z   @µїАЁ Џ 5 f‘сH¶Ѓ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x7bЖhPб c   c   E  c   @µЦАЁ ; 5 OЮп
# # # Ѓ       wqwtpbcom   wqwtpbcom      < 7H9nc1ICTirnaIQH4uz9Жh<е z   z   E  z   @µїАЁ Aћ 5 fВЦимЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x37ЖhUй g   g   E  g   @µТАЁ 8 5 SdvФЃ       gijw8ou0xyz   gijw8ou0xyz      < JaMPNKy8McCTlFh5xe2QЖhgн o   o   E  o   @µКАЁ ‡+ 5 [Q@M„Ѓ       n0iydh6jq2vwnet   n0iydh6jq2vwnet      < uWVmQ1U5aegw7IgZYV1SЖhPс z   z   E  z   @µїАЁ =W 5 f(I‡БЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x37ЖhGх g   g   E  g   @µТАЁ )l 5 S>'3Ѓ       	qpy2q16vdru   	qpy2q16vdru      < ojgJ8sOLPJbb7VQcGbqRЖh‹щ z   z   E  z   @µїАЁ €й 5 fЭO›Ѓ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x67Жh§э o   o   E  o   @µКАЁ Щ5 5 [њЎ8Ѓ       z28zt55tjgu7lol   z28zt55tjgu7lol      < DCSsfctF89WU8jVZrhjSЖhҐ a   a   E  a   @µШАЁ ‘в 5 M№`ЕЏЃ       3yjmjlol   3yjmjlol      < yhZlSkaVd6Bjm8vfx7j6ЖhР z   z   E  z   @µїАЁ oц 5 f·cёЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x33Жhй
# # #  m   m   E  m   @µМАЁ ‰ 5 Yй\Ѓ       19j65y6k8finet   19j65y6k8finet      < iJFZwTleahUPQIihv2CqЖhд i   i   E  i   @µРАЁ ж 5 U‰Џк0Ѓ       	6urqxwa1dcom   	6urqxwa1dcom      < YL0YtRGGyr4bKcdfVNgKЖhК z   z   E  z   @µїАЁ хD 5 fsЃдЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x6cЖh® g   g   E  g   @µТАЁ  5 SЯ6S
# # # Ѓ       nf7yb83hlol   nf7yb83hlol      < 3AYH2TX3HuoxRYmE6SsAЖhї m   m   E  m   @µМАЁ xъ 5 Yв.@ЛЃ       riijqvv0q2klol   riijqvv0q2klol      < 6kk4voSGF4dU9EaOesAlЖh`" z   z   E  z   @µїАЁ 2М 5 fNdi1Ѓ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x67Жh_& k   k   E  k   @µОАЁ %x 5 WА±пЯЃ   
# # # 0wwc80y6qsxyz   
# # # 0wwc80y6qsxyz      < 9TEZR1H2SisbICblmxPfЖhX* z   z   E  z   @µїАЁ Ш  5 fsХћЌЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x65ЖhE. a   a   E  a   @µШАЁ ^В 5 MмфѕУЃ       3ez26net   3ez26net      < abyX19yonBKqji8xvPXtЖh72 z   z   E  z   @µїАЁ ‚° 5 fE["XЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x65Жh%6 i   i   E  i   @µРАЁ t} 5 UтHґIЃ       	h902461e3net   	h902461e3net      < 0mbMfke1FgDkyiBlgsNyЖh%: c   c   E  c   @µЦАЁ ЧС 5 Old9+Ѓ       v5dgjoorg   v5dgjoorg      < KFYON34RBw2MzJFketYLЖh> z   z   E  z   @µїАЁ № 5 fЇУЂ_Ѓ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x7aЖhрA o   o   E  o   @µКАЁ ґc 5 [rнєЃ       nr3tadibmqaxlol   nr3tadibmqaxlol      < tTRF3VsANCDlCnUEgnrpЖhпE e   e   E  e   @µФАЁ  5 QддaжЃ       7wg3hnulol   7wg3hnulol      < sTrLI2ILKhIhTaWCKtFVЖh?J z   z   E  z   @µїАЁ ZР 5 fRК<ЙЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x65Жh%N a   a   E  a   @µШАЁ 3Є 5 M‡nЦЃ       n5wwjlol   n5wwjlol      < jg8Cgrvsdao216mPkZmqЖh
# # # R z   z   E  z   @µїАЁ ®5 5 fСXjШЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x62ЖhоU e   e   E  e   @µФАЁ  5 QдфАЃ       32ts9nalol   32ts9nalol      < rEv3AvT52O5SgZc1s6QtЖhюY m   m   E  m   @µМАЁ `f 5 Yр]ИЃ       6robxqjejnonet   6robxqjejnonet      < 8ujsnx7gu5juTTEH6KQMЖhЫ] z   z   E  z   @µїАЁ Нa 5 fЉN’µЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x63Жhnb g   g   E  g   @µТАЁ ѓШ 5 SHX ьЃ       51y5slzmcom   51y5slzmcom      < WiS9KQUGnFvleruuAwS8Жh„f _   _   E  _   @µЪАЁ nШ 5 Kb4њ1Ѓ       47nexru   47nexru      < TojyytkITxtkeZ8vRFEcЖh„j z   z   E  z   @µїАЁ яB 5 fЊM]ФЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x74Жhn i   i   E  i   @µРАЁ | 5 UеЕMUЃ       	0q2eaf52ccom   	0q2eaf52ccom      < K12VXcamrQLOiA9LKJdXЖhЗr z   z   E  z   @µїАЁ 4ю 5 fќ,Ѓ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x6bЖh v e   e   E  e   @µФАЁ ёІ 5 QСсUєЃ       u0mgzyhxyz   u0mgzyhxyz      < GVPaVaKQX7InergXtV75ЖhЋz z   z   E  z   @µїАЁ n 5 fЩд Ѓ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x61Жh…~ o   o   E  o   @µКАЁ L• 5 [@|QЃ       ep6m69494t3tlol   ep6m69494t3tlol      < H2EqT30mRSee4xLKYiDcЖhц‚ z   z   E  z   @µїАЁ &и 5 fqЎTЪЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x35Жh‡ k   k   E  k   @µОАЁ 5 5 Wll/їЃ       3bj3roe5ft3ru   3bj3roe5ft3ru      < jph4AeKsRDX0YOntgDevЖh‹ z   z   E  z   @µїАЁ 1л 5 f®u
# # # Ѓ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x30ЖhнЋ a   a   E  a   @µШАЁ   5 MўРҐ6Ѓ       trb4alol   trb4alol      < hGkc75fheKpG1cXQf3zNЖhж’ i   i   E  i   @µРАЁ Ѓ 5 UС9МЃ       	fiztt9z8xxyz   	fiztt9z8xxyz      < pg9BbPmZwVaCOcPfHSNXЖhф– z   z   E  z   @µїАЁ hР 5 fп‘Ѓ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x76Жhx› o   o   E  o   @µКАЁ Бс 5 [њтVґЃ       g20rzvi8vfi1org   g20rzvi8vfi1org      < VLPieK3xe3GTsMaYlxs3ЖhКџ z   z   E  z   @µїАЁ Ыѓ 5 fЙEСЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x65Жh№Ј m   m   E  m   @µМАЁ  5 Y[;5Ѓ       1yc7g2hea94com   1yc7g2hea94com      < uHgCmNjje0IfBDW8YlhQЖhЛ§ z   z   E  z   @µїАЁ “• 5 f
# # # ХNщЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x35ЖhЅ« e   e   E  e   @µФАЁ 2Ф 5 Q#'PWЃ       bjrwu7jorg   bjrwu7jorg      < ZEYdzwgGay5oQ7RyYfbdЖh¤Ї z   z   E  z   @µїАЁ V8 5 f•ХRЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x39Жh”і _   _   E  _   @µЪАЁ  W 5 KйћяЃ       zpr0uru   zpr0uru      < GONb7JA8kc2B4LR2jnuJЖh©· z   z   E  z   @µїАЁ 7 5 ft«=фЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x6aЖh°» a   a   E  a   @µШАЁ Ћ% 5 M№МЃ       fw9odorg   fw9odorg      < b0qcVLX0dcr9wWxm2ARLЖhА c   c   E  c   @µЦАЁ Сз 5 OЮЅ<GЃ       9qr6pr4ru   9qr6pr4ru      < PhnOYUiQQCAlNdn8IhfsЖhсГ z   z   E  z   @µїАЁ    5 fiLЂлЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x6aЖhИ m   m   E  m   @µМАЁ П 5 Yl6аЙЃ       f1shffdupu0xyz   f1shffdupu0xyz      < 6PIVpE8xTpw7AHqvjSdgЖhМ z   z   E  z   @µїАЁ }h 5 fTґЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x6aЖhР a   a   E  a   @µШАЁ +И 5 M‹CnSЃ       qi25bnet   qi25bnet      < XCvw5WTkniuYNMyFLccBЖhъУ c   c   E  c   @µЦАЁ Фb 5 Oф<Я[Ѓ       4x90c6net   4x90c6net      < b7q9ItoOrcae0GJnelCOЖhШ z   z   E  z   @µїАЁ эе 5 fюFо7Ѓ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x64ЖhљЬ o   o   E  o   @µКАЁ €Т 5 [ѓqXЃ       pr0dlflmnl8mcom   pr0dlflmnl8mcom      < HsAhu6ppvR0G8ePNkFiPЖhЂб z   z   E  z   @µїАЁ ‡с 5 fа№ЃЊЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x6aЖhче c   c   E  c   @µЦАЁ 	y 5 OМ Z\Ѓ       g0lz4elol   g0lz4elol      < CqDExfQBgyvwowCENWV3Жh{к z   z   E  z   @µїАЁ јJ 5 fiъЗЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x37Жh†о m   m   E  m   @µМАЁ ѕ] 5 Yіь}Ѓ       yybh2889mnuiru   yybh2889mnuiru      < BRI0CU41cY2ayQKtcyxWЖh‰т z   z   E  z   @µїАЁ KҐ 5 fG‰yЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x63Жhч e   e   E  e   @µФАЁ Їq 5 QЋ•шЃ       uyn0hoenet   uyn0hoenet      < bnuzfE8X7RvXSsFnTCcMЖh¦ы e   e   E  e   @µФАЁ 7k 5 QЎO;»Ѓ       m9l6odxorg   m9l6odxorg      < NCC7wZzvSDkhpsfUAkFjЖhЛя z   z   E  z   @µїАЁ З 5 fЉ";Ѓ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x73Жhя e   e   E  e   @µФАЁ \r 5 Qg(ЭґЃ       qr764e8org   qr764e8org      < ErJyWwy1YTZxd4VE981iЖh! i   i   E  i   @µРАЁ 8п 5 U„qµcЃ       	pl01pww9ylol   	pl01pww9ylol      < y58aFFWacoSYxLvOLfMsЖh  z   z   E  z   @µїАЁ 3 5 fRюЉ0Ѓ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x37Жh. m   m   E  m   @µМАЁ р 5 Y§VЏ¤Ѓ       g6812foeyaxorg   g6812foeyaxorg      < RwQCDOBSr6n2zZXbwukUЖhЭ _   _   E  _   @µЪАЁ -F 5 K%[/вЃ       ggxm5ru   ggxm5ru      < LQtokHgTUyCR6k86cgjMЖhµ z   z   E  z   @µїАЁ ¶€ 5 f™FЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x61ЖhЏ a   a   E  a   @µШАЁ P' 5 MЄМїyЃ       7zf2xorg   7zf2xorg      < PldbLiqVcU5RzGAmNspgЖhЂ  a   a   E  a   @µШАЁ M) 5 Mњd+Ѓ       d9mkeorg   d9mkeorg      < RKmfycVE1TWu5LcZXE2BЖh $ z   z   E  z   @µїАЁ жo 5 fЅ>FІЃ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x68Жh—( o   o   E  o   @µКАЁ * 5 [#п¦ЉЃ       u1f3f13d6e0ucom   u1f3f13d6e0ucom      < 2OfRzIqocVZcGzQ9KBslЖhі, g   g   E  g   @µТАЁ І­ 5 SябыЃ       znkco7iynet   znkco7iynet      < 2ratYn3qfYmw9iGTWQDmЖhА0 z   z   E  z   @µїАЁ kw 5 fК–і&Ѓ       otborinfosecmoscow   otborinfosecmoscow      < Your flag char is: 0x7dЖhУ4 i   i   E  i   @µРАЁ Re 5 UбZъ Ѓ       	bs4cakdcccom   	bs4cakdcccom      < 8jOweTlaSwdLnSgi2ck9
# # # """
# # #
# # # # Ищем все вхождения "Your flag char is: ..."
# # # matches = re.findall(r'Your flag char is: (0x[0-9a-f]+)', s, re.IGNORECASE)
# # #
# # # # Выводим найденные значения
# # # print("Все hex-значения после 'Your flag char is:':")
# # # for i, match in enumerate(matches, 1):
# # #     print(f"{i}: {match}")
# # #
# # # # Преобразуем hex в символы и собираем флаг
# # # flag = ''.join([chr(int(hex_val.replace('0x', ''), 16)) for hex_val in matches])
# # # print(f"\nСобранный флаг: {flag}")
# # s = """0x76
# # 0x73
# # 0x6f
# # 0x73
# # 0x68
# # 0x7b
# # 0x34
# # 0x6f
# # 0x67
# # 0x76
# # 0x74
# # 0x6f
# # 0x68
# # 0x38
# # 0x61
# # 0x77
# # 0x30
# # 0x39
# # 0x73
# # 0x38
# # 0x73
# # 0x6e
# # 0x61
# # 0x78
# # 0x72
# # 0x64
# # 0x72
# # 0x6c
# # 0x32
# # 0x77
# # 0x7a
# # 0x62
# # 0x77
# # 0x7d"""
# # print(s)
# hex_list = [
#     '0x76', '0x73', '0x6f', '0x73', '0x68', '0x7b', '0x34', '0x6f',
#     '0x67', '0x76', '0x74', '0x6f', '0x68', '0x38', '0x61', '0x77',
#     '0x30', '0x39', '0x73', '0x38', '0x73', '0x6e', '0x61', '0x78',
#     '0x72', '0x64', '0x72', '0x6c', '0x32', '0x77', '0x7a', '0x62',
#     '0x77', '0x7d'
# ]
#
# # Преобразование в символы
# flag = ''.join([chr(int(h, 16)) for h in hex_list])
# print(flag)
