def increasingSubarray(A):
    longest = []
    start = 0
    for i in range(1,len(A)):
        if A[i] - A[i-1] > 0:
            if len(longest) < i-start + 1:
                longest = A[start:i+1]
        else:
            start = i
    return longest

def lca(root,node1,node2):
    if root == node1 or root == node2:
        return root
    if root == None:
        return None
    leftlca  = lca(root.left,node1, node2)
    rightlca = lca(root.right,node1, node2)
    if leftlca and rightlca:
        return root
    if leftlca:
        return leftlca
    if rightlca:
        return rightlca
    return None

def rootToPath(root, node):
    path = []
    def exist(root):
        if root == None:
            return False
        if root == node or exist(root.left) or exist(root.right):
            path.append(root)
            return True
        return False
    exist(root)
    return path


def lca(root, node1, node2):
    if not root:
        return None
    if root == node1 or root == node2:
        return root
    leftlca = lca(root.left, node1, node2)
    rightlca = lca(root.right, node1, node2)
    if leftlca and rightlca:
        return root
    if leftlca:
        return leftlca
    if rightlca:
        return rightlca
    return None


def diameterTree(root):
    def height(root):
        if root == None:
            return 0
        return max(height(root.left), height(root.right))+1
    if not root:
        return 0
    return max(height(root.left)+height(root.right)+1, diameterTree(root.left), diameterTree(root.right))
height_map = {}
def diameter(root):
    def height(node):
        if not node:
            return 0
        if node in height_map:
            return height_map[node]
        h = max(height(node.left), height(node.right))+1
        height_map[node] = h
        return h
    if root == None:
        return 0
    return max(height(root.left)+height(root.right)+1, diameterTree(root.left), diameterTree(root.right))


