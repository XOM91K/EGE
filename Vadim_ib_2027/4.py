# s = 'wqe	"8.4\036/$$%\0365.\036538\036) 3%$3\036#3.psr"	tasks.mshp-ctf.ru	/	Сеанс	49 Б			'
s = b'8.4\036/$$%\0365.\036538\036) 3%$3\036#3.psr'
text = 'A' * 100
for x in s:
    print(chr(x ^ ord('A')), end='')
print(list(s))
#config.SECRET_KEY = 'you_need_to_try_harder_bro123'