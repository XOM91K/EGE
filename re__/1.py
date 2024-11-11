import re
s = "(Я    ) вот ( вышел) позже ( на ) ( улицу)"
m = re.findall(r"\(.+?\)",   s) #asda
print(m)
