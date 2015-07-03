__author__ = 'effy'
# -*- coding: utf-8 -*-

GRAY, BLACK = 0, 1
CYCLE = False
def topologicalsort(directed_graph):
    order, unvisited, state = [], set(directed_graph), {}
    def dfs(node):
        state[node] = GRAY
        for neighbor in directed_graph[node]:
            st = state.get(neighbor,None)
            if st == GRAY:
                CYCLE = True
                return False
            elif st == BLACK:
                continue
            else:
                unvisited.discard(neighbor)
                dfs(neighbor)
            order.append(node)
        state[order] = BLACK
    while unvisited:
        dfs(unvisited.pop())
    return order



def isCircle(string):
    def go(direction, cur):
        if direction == 0:
            cur[0] += 1
        if direction == 1:
            cur[1]  += 1
        if direction == 2:
            cur[0] -= 1
        if direction == 3:
            cur[1] -= 1
        return cur
    start,cur  = [0,0], [0,0]
    ##0 is right 1 is uo, 2 is left, 3 is down
    direction = 0
    for i in string:
        if i == 'G':
            cur =go(direction,cur)
        if i == 'L':
            direction  = (direction+1)%4
        if i == 'R':
            direction -= 1
            if direction < 0: direction = 3
    if cur == start:
        return True
    return False
#print isCircle('GLGLGLG')



def LCS(s1, s2):
    m,n = len(s1), len(s2)
    max_len = 0
    ## dp[i][j] is the length of common suffix of of s1[:i] and s2[:j]
    dp = [ [0 for i in range(m+1)] for j in range(n+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_len = max(max_len, dp[i][j])
    return max_len

def halfhalf(string):
    l = len(string)
    dp = [ [0 for i in range(l)] for j in range(l)]
    longest = 0

    for i in range(l):
        dp[i][i] = string[i]
        for j in range(i,l):
            dp[i][j] = dp[i][j-1] + int(string[j])
            if not (j-i+1)%2 and dp[i][(i+j-1)/2] *2 == dp[i][j]:
                longest = max(longest, j-i+1)
    return longest


def sumList(l):
    if l.__class__.__name__ == 'int':
        return l
    else:
        sum = 0
        for i in l:
            sum += sumList(i)
        return sum
#print sumList([1,[1,2,[3,4]],[5,6,7,[4,3,[4]]]])

def diameterTree(root):
    def height(root):
        if root == None:
            return 0
        return max(height(root.left), height(root.right))+1
    if not root:
        return 0
    return max(diameterTree(root.left), diameterTree(root.right), height(root.left)+height(root.right)+1)

def rootToNode(root,node1):
    path = []
    def dfs(r,node):
        if not r:
            return False
        if r == node or dfs(r.left, node) or dfs(r.right, node):
            path.append(r)
            return True
        return False
    dfs(root,node1)
    return path

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None

a,b,c,d,e,f,g = TreeNode(1),TreeNode(2),TreeNode(3),TreeNode(4),TreeNode(5),TreeNode(6),TreeNode(7)
a.left,a.right, b.left,b.right,c.left,c.right = b,c,d,e,f,g
#x = rootToNode(a,e)
'''
print x.__class__.__name__
for i in x:
    print i.val
'''
'''

The method 1 finds LCA in O(n) time, but requires three tree traversals plus extra
spaces for path arrays. If we assume that the keys n1 and n2 are present in Binary Tree,
we can find LCA using single traversal of Binary Tree and without extra storage for path arrays.
The idea is to traverse the tree starting from root. If any of the given keys (n1 and n2)
matches with root, then root is LCA (assuming that both keys are present).
If root doesn’t match with any of the keys, we recur for left and right subtree.
 The node which has one key present in its left subtree and the other key present in right subtree is the LCA.
 If both keys lie in left subtree, then left subtree has LCA also, otherwise LCA lies in right subtree.
'''
def lowestCommonAncestor(root,node1,node2):
    if root == None:
        return None
    if root == node1 or root == node2:
        return root
    leftlca = lowestCommonAncestor(root.left, node1, node2)
    rightlca = lowestCommonAncestor(root.right, node1, node2)
    if leftlca and rightlca:
        return root
    else:
        if leftlca:
            return leftlca
        if leftlca:
            return rightlca
        return None


def ways_dp(amount, deno):
    total_ways = [0 for i in range(amount+1)]
    total_ways[0] = 1
    deno.sort()
    for coin in deno:
        for money in xrange(coin,amount+1):
            print coin, money
            total_ways[money]+=total_ways[money-coin]
    return total_ways[-1]
#print ways_dp(4,[1,2,3])

def recoverPath(adjacent, start,end):
    visited = {key:False for key in adjacent}
    res = []
    def dfs(path, cur):
        print cur, path
        visited[cur] = True
        if cur == end:
            res.append(path)
        else:
            for neighbor in adjacent[cur]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(path+[neighbor], neighbor)
            visited[cur] = False
            path = path[:-1]

    dfs([start], start)
    return res
#print recoverPath({'A':['B'],'B':['C'], 'C':['D','F'], 'D':['E'], 'E':['B'], 'F':[]}, 'A', 'F')

def recoverPath(start, end, path):
    start_node = {}
    for i in range(len(path)):
        start_node[path[i][0]] = start_node.get(path[i][0], []) + [i]
    edge_visited = [False for i in range(len(path))]
    p = [start]
    def dfs(cur):
        print p, cur
        if cur == end and all(edge_visited):
            return True
        else:
            for e in start_node[cur]:
                if not edge_visited[e]:
                    edge_visited[e] = True
                    p.append(path[e][1])
                    if dfs(path[e][1]):
                        return True
                    edge_visited[e] = False
                    p.pop()
            return False
    if dfs(start):
        return p

start = 'a'
end = 'f'
paths = [('b', 'c'), ('d', 'e'), ('a', 'b'), ('c', 'd'), ('e', 'b'), ('b', 'c'), ('c', 'f')]
print recoverPath('a','f', paths)