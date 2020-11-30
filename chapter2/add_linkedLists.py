class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        elems = []
        current = self.head
        while current != None:
            elems.append(current)
            current = current.next
        return elems

    def append(self, item):
        elem = Node(item)
        if self.head == None:
            self.head = elem
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = elem

    def addTwoLists(self, first, second):
        head = third = Node(0)
        carry = 0

        while first or second or carry:
            if first:
                carry += first.data
                first = first.next
            if second:
                carry += second.data
                second = second.next

            third.data = carry % 10
            carry = carry // 10

            if first or second or carry:
                third.next = Node(0)
                third = third.next
        return head






ll = LinkedList()
list1 = LinkedList()
list2 = LinkedList()
list1.append(7)
list1.append(1)
list1.append(6)
# print(list1.display())
list2.append(5)
list2.append(9)
list2.append(2)
print(list2.display())
print(ll.addTwoLists(list1,list2))
# print(ll.display())


