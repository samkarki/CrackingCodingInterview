import sys
sys.path.append(".")
from LinkedList import *

def kth_lastElem(alist, index):
    '''pass index = 1 return the last element index = 2 returns second last element and so on'''

    length = alist.size()
    if index >= length:
        print("Index out of range")

    else:
        current = alist.head
        while current != None:
            if length == index:
                return current.data
            length = length - 1
            current = current.next
print(ll.print_Linkedlist())
print(kth_lastElem(ll, 5))


