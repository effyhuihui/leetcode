class LinkedList:
	def __init__(self, val):
		self.val = val
		self.next = None

def deleteDuplicates(head):
	'''
	Given a sorted linked list, delete all duplicates such that each element appear only once.

	For example,
	Given 1->1->2, return 1->2.
	Given 1->1->2->3->3, return 1->2->3.
	'''
	if not head:
		return head
	node = head.next
	pre_value = head.val
	pre_node = head
	while node:
		if node.val == pre_value:
			node = node.next
			pre_node.next = node
		else:
			pre_node = node
			pre_value = node.val
			node = node.next
	return head

a = LinkedList(1)
b = LinkedList(2)
a.next = b
head = deleteDuplicates(a)
print head.val