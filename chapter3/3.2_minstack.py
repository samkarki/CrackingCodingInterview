
class Stack:
    def __init__(self):
        self.stack = []
        self.minstack =[]

    def push(self, value):
        self.stack.append(value)

        if self.minstack == [] or value <self.minm():
            self.minstack.append(value)

    def pop(self):
        if self.stack ==[]:
            return None
        else:
            self.stack.pop()
            self.minstack.pop()

    def minm(self):
        if self.minstack==[]:
            return None
        else:
            return self.minstack[-1]
s = Stack()
s.push(0)
s.push(2)
s.push(-1)
s.push(6)
s.push(12)
print(s.minm())


