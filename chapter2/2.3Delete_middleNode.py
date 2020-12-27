import sys
sys.path.append(".")
from LinkedList import *

#time complexity O(n)
def deleteMidnode(alist, node):
    current = alist.head
    previous = None


    while current != None:
        if current.data == node:
            previous.next = current.next
            # current = current.next
        previous= current
        current = current.next

print(ll.print_Linkedlist())
deleteMidnode(ll, 3)
print(ll.print_Linkedlist())

#the code gives error when the node is first and last, as required
#not sure how to raise an error when the node is the first and last element