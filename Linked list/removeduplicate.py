from llist import *

def duplicate(head):
    curr = head
    if curr is None:
        return None
    while curr.next is not None:
        if curr.data == curr.next.data:
            nexct = curr.next.next
            curr.next = None
            curr.next = nexct
        else:
            curr = curr.next
    return head