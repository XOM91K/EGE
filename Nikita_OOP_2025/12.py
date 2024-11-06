class Stack:
    def __init__(self):
        self.__stk = []
    def push_back(self, element):
        self.__stk.append(element)

    def pop_back(self):
        del self.__stk[-1]

    def get_stack(self):
        return self.__stk

    def __len__(self):
        return len(self.__stk)

stk = Stack()
print(stk.get_stack())
stk.push_back(10)
stk.push_back(20)
stk.pop_back()
print(stk.get_stack())
print(len(stk))