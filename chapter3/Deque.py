class Deque:
    def __init__(self):
        self.items =[]

    def __str__(self):
        temp_str = "Rear--> "
        for item in self.items:
            temp_str += str(item) + " "
        return temp_str + "<--Front"

    def isEmpty(self):
        return self.items ==[]

    def add_Front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        return self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

d = Deque()
d.add_Front(1)
d.add_Front(9)
d.add_Front(13)
d.add_rear(27)
d.add_rear(45)
d.add_rear(12)
print(d)
d.remove_rear()
d.remove_front()
print(d)
