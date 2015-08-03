def twosum(root, target):
	def dfs(root1, root2, target):
		if not root1 or not root2:
			return False
		if root1.val+root2.val == target and  root1 != root2:
			return True
		if root1.val + root2.val > target:
			if root1 == root2:
				return dfs(root1.left,root)
			else:
				return dfs(root1.left,root2) or dfs(root1, root2.left)
		else:
			if root1 == root2:
				return dfs(root1.right,root2)
			else:
				return dfs(root1.right,root2) or dfs(root1, root2.right)



def lowestAncestor(a,b,root):
	## if rootval = a or b, root is LCA
	## if min(a,b) < rootval < max(a,b), root is LCA
	if not root:
		return None
	rootval = root.val
	if rootval > max(a,b):
		return lowestAncestor(a,b,root.left)
	elif rootval < min(a,b):
		return lowestAncestor(a,b,root.right)
	return root



def printtable(n):
	res = []
	for i in range(1,n+1):
		res.append([])
		for j in range(i,n+1):
			res[-1].append(i*j)
	print res

printtable(5)






































