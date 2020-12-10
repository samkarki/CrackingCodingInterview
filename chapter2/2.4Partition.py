import sys
sys.path.append(".")
from LinkedList import *

def partition(alist, node):  # time complexity O
    current = alist.head
    lessthannode = LinkedList([0])
    equalnode = LinkedList([0])
    greaternode = LinkedList([0])

    while current != None:
        if current.data < node:
            if lessthannode.head == None:
                lessthannode.head = node
            else:
                current = lessthannode.head
                while current != None:
                    current.next = node

        elif current.data == node:
            if equalnode.head == None:
                equalnode.head = node
            else:
                current = equalnode.head
                while current != None:
                    current.next = node

        else:
            if greaternode.head == None:
                greaternode.head = node
            else:
                current =greaternode.head
                while current != None:
                    current.next = node

        current = current.next
    return (lessthannode + equalnode + greaternode)



print(ll.print_Linkedlist())
print(partition(ll, 3))