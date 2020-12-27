class setofPlates:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def __str__(self):
        return str(self.stacks)

    def push(self, item):
        if self.stacks == []:
            self.stacks.append([item])
        else:
            if len(self.stacks[-1]) >= self.capacity:
                self.stacks.append([item])
            else:
                self.stacks[-1].append(item)
    def pop(self):
        if self.stacks == []:
            return IndexError("pop from Empty stack not allowed")
        else:
            popped_value = self.stacks[-1][-1]
            if len(self.stacks[-1]) == 1:
                del self.stacks[-1]
            else:
                del self.stacks[-1][-1]
        return popped_value

    def pop_at(self, index):
        if self.stacks == []:
            return NameError("can't pop from empty stack")

        elif index -1 > len(self.stacks):
            return NameError("Index out of range")

        else:
            popped_value = self.stacks[index-1][-1]
            if len(self.stacks[index-1]) == 1:
                del self.stacks[-1]
            elif len(self.stacks) == index:
                del self.stacks[-1][-1]
            else:
                self.stacks[index-1][-1] = self.stacks[index][0]

                for i in range(index, len(self.stacks)):
                    for j in range(0, len(self.stacks[i]) - 1):
                        self.stacks[i][j] = self.stacks[i][j+1]
                    if i < len(self.stacks) -1:
                        self.stacks[i][-1] = self.stacks[i+1][0]

                del self.stacks[-1][-1]
                if len(self.stacks[-1]) == 0:
                    del self.stacks[-1]

            return popped_value



s = setofPlates(4)
s.push(3)
s.push(5)
s.push(4)
s.push(7)
s.push(0)
print(s)
print(s.pop_at([-1][0]))
print(s.pop())

print(s)
