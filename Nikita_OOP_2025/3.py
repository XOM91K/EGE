class Bell:
    def __init__(self, *args, **kwargs):
        self.sl = sorted(kwargs.items())
        self.sl1 = args
        self.arg = args

    def print_info(self):
        d = []
        for i in self.sl:
            d.append(f'{i[0]}: {i[1]}, ')
        d = ''.join(d)[:-2]
        g = ''
        for y in self.sl1:
            g += y + ', '
        if len(d) == 0:
            print(g[:-2])
        elif len(d) > 0 and len(g) > 0:
            print(d + '; ' + g[:-2])
        elif len(g) == 0 and len(d) > 0:
            print(d)


class BellTower:
    def __init__(self, *args, **kwargs):
        self.bells = list(args)
        # self.sl1 = args
        # self.sl2 = sorted(kwargs.items())

    def append(self, bell):
        self.bells.append(bell)

    def sound(self):
        for x in self.bells:
            x.sound()
        print('...')


class BigBell(Bell):
    def __init__(self, *args, **kwargs):
        self.flag = 1
        self.sl1 = args
        self.sl = sorted(kwargs.items())

    def sound(self):
        if self.flag % 2 == 1:
            print('ding')
        else:
            print('dong')
        self.flag += 1


class LittleBell(Bell):
    def sound(self):
        print('ding')


Bell("бронзовый").print_info()
LittleBell("медный", нота="ля").print_info()
BigBell(название="Корноухий", вес="1275 пудов").print_info()
