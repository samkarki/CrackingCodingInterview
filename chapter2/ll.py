class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        node = []

        while current != None:
            node.append(current.data)
            current = current.next
        return node

    def append(self, data):
        elem = Node(data)
        if self.head == None:
            self.head = elem
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = elem

    def add_atFront(self, data):
        elem = Node(data)
        if self.head == None:
            self.head = elem
        else:
            elem.next = self.head
            self.head = elem

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current= current.next
        return count

    # def erase(self, data):
    #     current = self.head
    #     previous = None
    #
    #     while current != None:
    #         if current.data == data:
    #             if current == self.head:
    #                 self.head = self.head.next
    #             else:
    #                 previous.next = current.next
    #         previous = current
    #         current = current.next
    #
    def get(self, index):#review this
       if index >= self.length():
           print("Index out of range")
       else:
           current = self.head
           current_index = 0

           while current != None:
               if current_index == index:
                   return current.data
               current_index += 1
               current = current.next
    def addAfter(self, data, newnode):
        node = Node(newnode)

        current = self.head
        while  current != None:
            if current.data == data:
                newnode.next = current.next
                current.next = newnode
            current = current.next

    def insert(self, data , index):#review this
        elem = Node(data)
        if index == 0:
            elem.next = self.head
            self.head = elem
        else:
            current = self.head
            current_index = 0
            while current != None and current_index < index-1:
                current = current.next
                current_index +=1

            if current == None:
                print("Index error")
            else:
                elem.next = current.next
                current.next = elem

    # def remove(self,index):# review this
    #     if index == 0:
    #         self.head = self.head.next
    #
    #     else:
    #         current_index = 0
    #         current = self.head
    #         while current != None and current_index < index- 1:
    #             current = current.next
    #             current_index += 1
    #         temp = current
    #         current = current.next
    #         if current_index == index:
    #             temp.next = current.next

    # def search(self, data):
    #     current = self.head
    #     while current !=None:
    #         if current.data == data:
    #             return True
    #         current = current.next
    #     return False
    #
    # def removeDup(self):#time complexity space complexity 6
    #     current = self.head
    #     previous = None
    #     elems = []
    #     while current != None:
    #         if current.data in elems:
    #             previous.next= current.next
    #             current = current.next
    #         else:
    #             elems.append(current.data)
    #             previous = current
    #             current = current.next
    #
    # def print_nth_fromLast(self, index):
    #     # k= 1 , which returns first element, k= 2 , returns second elment
    #     length = self.length()
    #     #print(length)
    #     current = self.head
    #
    #     while current != None:
    #         if length == index:
    #             return current.data
    #         length -= 1
    #         current = current.next
    #     # if current is None:
    #     #     return None
    #
    #
    # def removeNode(self, node):
    #      current = self.head
    #      previous =None
    #
    #      while current!= None:
    #          if current.data == node:
    #              previous.next = current.next
    #
    #          previous = current
    #          current = current.next
    #
    #      if current is None:
    #          return
    #
    def partition(self, x):
        current= self.head
        before = before_head = Node(0)
        after = after_head = Node(0)

        while current != None:
             # If the original list node is lesser than the given x,
            # assign it to the before list.
            if current.data < x:
                before.next = current
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = current
                after = after.next

            # move ahead in the original list
            current = current.next

        # Last node of "after" list would also be ending node of the reformed list
        after.next = None
        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        before.next = after_head.next

        return before_head.next

    def reverse(self):
        if self.head == None or self.head.next == None:
            return

        current = self.head
        previous = None
        while current != None:
            temp = current
            current= current.next
            temp.next = previous
            previous = temp
        self.head = previous

    def palindromeChecker(self):
        current = self.head
        elems = []
        flag = True

        while current != None:
            elems.append(current.data)
            current = current.next

        while current != None:
            i = elems.pop()
            if current.data == i:
                flag = True
            else:
                flag = False
                break

            current = current.next
        return flag



ll= LList()
print(ll.display())
ll.append(3)
ll.append(17)
ll.add_atFront(8)
ll.add_atFront(2)
ll.insert(5,0)
ll.insert(7,2)
print(ll.display())
ll.addAfter(0,1)


print(ll.display())
# ll.reverse()
# print(ll.palindromeChecker())


# print(ll.print_nth_fromLast(1))
# print(ll.print_nth_fromLast(6))
# ll.removeNode(7)
print(ll.partition(2))
# print(ll.display())
# ll.removeDup()
# print(ll.display())
# # ll.remove(0)
# # ll.remove(-1)
# # ll.erase(7)
# # ll.erase('Bare')
# # print(ll.display())
# # print(ll.length())
# print(ll.get(1))
# # print(ll.get(-1))
# print(ll.search(75))