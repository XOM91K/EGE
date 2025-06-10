from sf.structureTypes.one.array import MyIntArray
import unittest


class finderTest(unittest.TestCase):

    # test with a list sorted in ascending order
    def test(self):
        a = MyIntArray()

        a.pushBack(5)
        assert("Add element", a.get(a.getSize() - 1) == 5)
        a.popBack()
        print(a)


if __name__ == '__main__':
    unittest.main()