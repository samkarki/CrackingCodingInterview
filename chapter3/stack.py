class Stack:
    def __init__(self):
        self.items = []

    def __str__(self): # reference https://github.com/gsprint23/cpts215/blob/master/lessons/U2%20Algorithm-Analysis
        temp_str = "Bottom -->"
        for item in self.items:
            temp_str += str(item) + "  "
        return temp_str + " <--Top"

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
cities = Stack()
cities.push("Lewiston")
cities.push("Clarkston")
cities.push("Moscow")
cities.push("Pullman")
print(cities)
cities.push("Spokane")
cities.push("Seattle")
print(cities)
print("top_city: ", cities.pop())
print("top_city2: ", cities.peek())
while not cities.isEmpty():
    print(cities.pop())