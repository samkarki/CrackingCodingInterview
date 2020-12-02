
class Node:
     def __init__(self, data = None):
         self.data = data
         self.next = None

     def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def print_Linkedlist(self):
        node = []
        current = self.head
        while current != None:
            node.append(current.data)
            current = current.next
        return node

    def append(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    def add_Front(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def add_after(self, data, newNode):

        if self.head == None:
            return
        else:
            current = self.head
            while current != None:
                if current.data == data:
                    newNode.next =current.next
                    current.next = newNode
                current = current.next

    def add_before(self, data, newNode):

        if self.head == None:
            return

        if self.head.data == data:
            newNode.next = self.head
            self.head = newNode
        else:
            previous = None
            current = self.head
            while current != None:
                if current.data == data:
                    previous.next = newNode
                    newNode.next = current
            previous = current
            current = current.next

    def traverse(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

    def size(self):
        current = self.head
        total_count = 0
        while current != None:

            current = current.next
            total_count += 1
        return total_count

    def getData(self, index):

        if index > self.size() or index < 0:
            print("Index out of range")

        else:
            current = self.head
            curr_Index = 0

            while current != None:
                if curr_Index == index:
                    return current.data

                curr_Index += 1
                current = current.next

    def insertValue(self, index, newNode):

        if index > self.size() or index < 0:
            print("Index out of range:")
            return

        if index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            current = self.head
            curr_Index = 0
            previous = None

            while current != None and curr_Index < index -1:
                current = current.next
                curr_Index += 1
            newNode.next = current.next
            current.next = newNode




ll = LinkedList()
# print(ll.print_Linkedlist())
ll.append(3)
ll.append(5)
ll.append(9)
ll.add_Front(12)
ll.add_after(12,Node(1))
ll.add_before(12, Node(0))
# print(ll.print_Linkedlist())
# ll.traverse()
# print(ll.size())
# print(ll.getData(0))
# print(ll.getData(1))
ll.insertValue(0 ,Node(5))
ll.insertValue(1 ,Node(2))
# print(ll.print_Linkedlist())

