class Bell:
    def __init__(self, *args, **kwargs):
        self.sl = sorted(kwargs.items())
        self.arg = args
    def print_info(self):
        d = []
        for i in self.sl:
            d.append(f'{i[0]}: {i[1]},')

class BellTower:
    def __init__(self, *args):
        self.bells = list(args)

    def append(self, bell):
        self.bells.append(bell)

    def sound(self):
        for x in self.bells:
            x.sound()
        print('...')


class BigBell(Bell):
    def __init__(self):
        self.flag = 1

    def sound(self):
        if self.flag % 2 == 1:
            print('ding')
        else:
            print('dong')
        self.flag += 1


class LittleBell(Bell):
    def sound(self):
        print('ding')
def F(*args, **kwargs):
    return args, sorted(kwargs.items())
print(F(а=5, в=5, б=5))