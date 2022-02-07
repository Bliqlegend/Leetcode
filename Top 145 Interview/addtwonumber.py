from Functions.llist import *

def TRASH(head1,head2):
    curr1 = head1
    curr2 = head2
    n1 = 0
    idx = 1
    while curr1 is not None:
        n1 += (curr1.data)*idx
        idx*=10
        curr1 = curr1.next
    n2 = 0
    idx = 1
    while curr2 is not None:
        n2+= (curr2.data)*idx
        idx*=10
        curr2 = curr2.next
    n = n1 + n2
    head = None
    tail = None
    o = []
    while n != 0:
        ele = int(n%10)
        n = int(n /10)
        o.append(ele)
    # Make LL
    for ele in o:
        if ele == -1:
            break
        newNode = Node(ele)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

def add2nums(head1,head2):
    result = Node(0)
    result_tail = result
    carry = 0

    while head1 or head2 or carry:
        val1 = (head1.data if head1 else 0)
        val2 = (head2.data if head2 else 0)

        carry,out = divmod(val1+val2+carry,10)
        result_tail.next  = Node(out)
        result_tail = result_tail.next

        head1 = (head1.next if head1 else None)
        head2 = (head2.next if head2 else None)
    return result.next


head1 = StakeInput()
head2 = StakeInput()
head = add2nums(head1,head2)
printLL(head)