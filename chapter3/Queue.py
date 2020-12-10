class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        temp_str = "Rear-->"
        for item in self.items:
            temp_str += str(item) + " "
        return temp_str + "<--Front"

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
q = Queue()
q.enqueue("Burgundy")
q.enqueue("Pastel")
q.enqueue("red")
q.enqueue("fuschia")
q.enqueue("green")
q.enqueue("emerald")
print(q)
print("Dequeing:" , q.dequeue())
print(q)


