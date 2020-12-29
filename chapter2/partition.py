
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_Linkedlist(self):
        node = []
        current = self.head
        while current != None:
            node.append(current.data)
            current = current.next
        return node

    def append(self, node):

        if self.head == None:
            self.tail = self.head = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        return self.tail

    def partition(self, data):
        current = self.tail = self.head

        while current :
            next_node = current.next
            # current.next = None
            if current.data < data:
                current.next = self.head
                self.head = current
            else:
                self.tail.next = current
                self.tail = current

            current = next_node

        if self.tail.next != None:
            self.tail.next = None




ll = LinkedList()
ll.append(Node(4))
ll.append(Node(0))
ll.append(Node(1))
ll.append(Node(7))
print(ll.print_Linkedlist())
ll.partition(2)
print(ll.print_Linkedlist())