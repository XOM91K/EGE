class BellTower:
    def __init__(self, *args):
        self.bells = list(args)

    def append(self, bell):
        self.bells.append(bell)

    def sound(self):
        for x in self.bells:
            x.sound()
        print('...')


class BigBell:
    def __init__(self):
        self.flag = 1

    def sound(self):
        if self.flag % 2 == 1:
            print('ding')
        else:
            print('dong')
        self.flag += 1


class LittleBell:
    def sound(self):
        print('ding')
