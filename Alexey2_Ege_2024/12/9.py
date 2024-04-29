for n in range(1,100):
   s = '>2' + '12' * n + '<'
   while '>2<' not in s:
       s = s.replace('>1', '>2', 1)
       s = s.replace('>21', '1>', 1)
       s = s.replace('12<', '1<2', 1)
       s = s.replace('1<', '<2', 1)
   if s.count('1') + s.count('2') * 2 > 103:
       print(n, s)