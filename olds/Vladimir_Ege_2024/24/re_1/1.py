import re
s = "<p style=\"margin-left:25px;font-weight:bold;color:#0f4375;\">"
m = re.findall(r"style=.+color:(.+);\">", s)
print(m) # . - абсолютно любой символ
# + - поиск от 1 до бесконечности символов
# () - сохраняющие группирующие скобки