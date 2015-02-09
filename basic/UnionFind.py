class QuickFindUF:
	'''
	This is a Union Find API that enables quick find, which means that 
	to check whetehr two elements are connected only takes O(1) time, but 
	Union operation is slow, one union takes O(N) time.

	Data Structure:
	maintain a list with index representing the node, and its value is one of 
	the node that in the linked group
	
	0---1     3
         \   / 	
  		  \ / 		The left diagram is represented as a list below
    7---6  5  4
        |_____|        [0, 0, 2, 0, 4, 0, 4, 4]
	'''
	def __init__(self, n):
		self.component = [i for i in range(n)]

	def connected(self,i,j):
		# O(1) time complexity
		return self.component[i] == self.component[j]

	def union(self, i, j):
		# O(N) time complexity
		a = self.component[i]
		b = self.component[j]
		if a != b:
			for k in range(len(self.component)):
				if self.component[k] == b: self.component[k] = a

a = QuickFindUF(8)
a.union(0,1)
a.union(0,5)
a.union(1,3)
a.union(6,7)
a.union(4,6)
print a.connected(0,5)
print a.component


class QuickUnionUF:
	def __init__(self,n):
		self.component = [i for i in range(n)]

	def root(self,i):
		while self.component[i] != i:
			i = self.component[i]
		return i

	def connected(self,i,j):
		return self.root(i) == self.root(j)




















