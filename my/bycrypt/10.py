import base64
s = 'n11z01sXq9815LtpN103Tam09Bqg81AyfoX013og9blV6W8jqkV1puw30r1qo5Px9i2B8t11l5Td98a4Tn10gr2F6m8cGl95r1Din1jT0l84Z9tei1Jb8eE40De9mj1Tg1i2D1k701ik8'
for x in '0189':
    s = s.replace(x, '')
s = s.upper()
print(base64.b32decode(s))
