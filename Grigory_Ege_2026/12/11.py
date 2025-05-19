x = '1' * 81
while '111' in x or '88' in x:
    if '88' in x :
        x = x.replace('88','1111')
    else:
        x = x.replace('111' , '8' )
print(x)