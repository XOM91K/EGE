import ctypes


class MyIntArray(object):

    def __init__(self):
        self.b = []

    def getSize(self):
        return len(self.b)

    def get(self, k):
        return self.b[k]

    def set(self, k, x):
        self.b.insert(k, x)

    def pushBack(self, ele):
        self.b.append(ele)

    def popBack(self):
        del self.b[-1]