__author__ = 'effy'
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

## iterative
def reverse(head):
  last = None
  current = head

  while current:
    next = current.next
    current.next = last
    last = current
    current = next

  return last


#Recursive To be validated!!!!!!
def recurse(head,last):
  if head is None:
    return last
  next = head.next
  head.next = last
  return recurse(next, head)

a,b,c,d,e = ListNode(1), ListNode(2),ListNode(3),ListNode(4), ListNode(5)
a.next,b.next,c.next,d.next = b,c,d,e
k = reverse(a)

while k:
    print k.val
    k = k.next

