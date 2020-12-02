import sys
sys.path.append(".")
from LinkedList import ll

# time complexity o(n), space complexity 0(n)
def removeDups(alist):
    elems = []

    previous = None
    current = alist.head
    while current != None:
        if current.data not in elems:
            elems.append(current.data)
            previous = current
            current = current.next

        else:
            previous.next = current.next
            current = current.next
    return elems

print(removeDups(ll))




