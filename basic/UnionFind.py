class QuickFindUF:
	'''
	This is a Union Find API that enables quick find, which means that 
	to check whetehr two elements are connected only takes O(1) time, but 
	Union operation is slow, one union takes O(N) time.

	Data Structure:
	maintain a list with index representing the node, and its value is one of 
	the node that in the linked group
	
	0---1  2  3
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
#print a.connected(0,5)
#print a.component


class QuickUnionUF:
	'''
	This is a Union Find API that enables quick union, which means that 
	to union two elements takes O(lgN) time, but it is relatively slow to 
	check wehther two elements are connected (takes O(lgN) time, but worst case still N) 

	In each union operation, we set q's root to p's root.
	Data Structure:
	maintain a list with index representing the node, and its value is its parent in
	the component tree.
	
	0---1  2  3
         \   / 	
  		  \ / 		The left diagram is represented as a list below
    7---6  5  4
        |_____|        [5, 3, 2, 3, 6, 5, 7, 7]


    so for 0-1-5-3 component set, the root is 5, for 7-6-4 component set, the root is 7
	'''
	def __init__(self,n):
		self.component = [i for i in range(n)]

	def root(self,i):
		while self.component[i] != i:
			i = self.component[i]
		return i

	def connected(self,i,j):
		return self.root(i) == self.root(j)

	def union(self,i,j):
		# set j's root to i's root
		## tree re-structure has to be root manipulate, meaning only root can
		## be set to the parent/child of another root. otherwise it could occur
		## that a child has more than one parent.
		p = self.root(i)
		q = self.root(j)
		self.component[q] = p

a = QuickUnionUF(8)
a.union(0,1)
a.union(0,5)
a.union(1,3)
a.union(6,7)
a.union(4,6)
#print a.connected(0,5)
print a.component

class WeightedQuickUnionUF:
	'''
	in the above QuickUnionUF class, one bad thing that could happend is that
	a component tree could be thin, tall, and very unbalanced -- like a linear 
	tree, which is the worst case, then connected() would be very slow. In order 
	to avoid this, in each union operation
	we always set p's root to q, regardless of what the tree looks like. What we 
	can do here is to add another array which keeps the size of the each tree

	Data Structure:
	two lists:
	1. the tree structure of connected components
	2. the size of each tree


	0---1  2  3     The left diagram is represented as a list below
         \   / 	     1. tree structure list [5, 3, 2, 3, 6, 5, 7, 7]
  		  \ / 		 2.   
    7---6  5  4
        |_____|        

	'''
	def __init__(self, n):
		self.component = [i for i in range(n)]
		self.treesize = [1 for i in range(n)]

	def root(self ,p):
		while self.component[p] != p:
			p = self.component[p]
		return p

	def union(self,p,q):
		i = self.root(p)
		j = self.root(q)
		if i == j :
			return
		a, b = self.treesize[i], self.treesize[j]
		if a > b:
			self.component[j] = i
			self.treesize[i] = a + b
		else:
			self.component[i] = j
			self.treesize[j] = a + b

class PathCompressionUF:
	'''
	Add one more step in addtion to the previous class
	During the course of finding root, set each examined node to root to flatten the tree
	'''




















