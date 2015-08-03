__author__ = 'effy'
# -*- coding: utf-8 -*-

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

'''
number of ways to adds up coins

'''
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


'''
Note that for an directed graph, it is not useful to keep track whether a node has been visted or not,
rather it is more important to keep track of whether an edge has been visted or not
find a path in an directed path from start to end
'''
def recoverPath(adjacent, start,end):
    edge_visited = {key:False for key in adjacent}
    for node in adjacent:
        for end in adjacent[node]:
            edge_visited[(node,end)] = False
    res = [start]
    def dfs(cur):
        if cur == end:
            return True
        for neighbor in adjacent[cur]:
            if not edge_visited[(cur,neighbor)]:
                edge_visited[(cur,neighbor)] = True
                res.append(neighbor)
                if dfs(neighbor):
                    return True
                edge_visited[(cur,neighbor)] = False
                res.pop()
        return False

    if dfs(start):
        return res
    return False
#print recoverPath({'A':['B'],'B':['C'], 'C':['D','F'], 'D':['E'], 'E':['B'], 'F':[]}, 'A', 'F')
'''
Euler's path --> input is an array of paired node, i.e. an edge
'''
def recoverPathOnce(start, end, path):
    ##directed graph
    adjacent_list = {}
    for i in range(len(path)):
        adjacent_list[path[i][0]] = adjacent_list.get(path[i][0], []) + [i]
    edge_visited = [False for i in range(len(path))]
    p = [start]
    def dfs(cur):
        print p, cur
        if cur == end and all(edge_visited):
            return True
        else:
            for e in adjacent_list[cur]:
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
    return False

start = 'a'
end = 'f'
paths = [('b', 'c'), ('d', 'e'), ('a', 'b'), ('c', 'd'), ('e', 'b'), ('b', 'c'), ('c', 'f')]
#print recoverPathOnce('a','f', paths)


'''
input is a stream of similar string pairs, return all words that are similar
(a,b), (b,c), (a,c) --> (a,b,c) are all similar
'''
class UFwords:
    def __init__(self):
        self.tree_map = {}
        self.count = 0

    def union(self,a,b):
        root_a = self.find(a)
        root_b = self.find(b)
        if not root_a and not root_b:
            self.tree_map[a] = a
            self.tree_map[b] = a
            self.count += 1
        elif root_a and root_b:
            self.tree_map[root_a] = root_b
            self.count -= 1
        else:
            if root_a:
                self.tree_map[b] = root_a
            if root_b:
                self.tree_map[a] = root_b

    def find(self,a):
        if a not in self.tree_map:
            return None
        ## path compression
        if self.tree_map[a] != a:
            self.tree_map[a] = self.find(self.tree_map[a])
        return self.tree_map[a]

    def clutser(self):
        inverted_map = defaultdict(list)
        for key in self.tree_map:
            root = self.find(key)
            inverted_map[root] += [key]
        return [cluster for cluster in inverted_map.itervalues()]


'''
number of islands variantion
'''
class UFislands:
    def __init__(self,m,n):
        self.board = [ [0 for i in range(n)] for j in range(m)]
        self.count = 0
        self.tree_map = {}

    def find(self,i,j):
        if (i,j) not in self.tree_map:
            return None
        if self.tree_map[(i,j)] != (i,j):
            self.tree_map[(i,j)] = self.find(self.tree_map[(i,j)])
        return self.tree_map[(i,j)]

    def union(self,a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if not root_b and not root_a:
            self.tree_map[a] = b
            self.count += 1
        elif root_a and root_b:
            self.tree_map[root_a] = root_b
            self.count -= 1
        else:
            if root_a:
                self.tree_map[root_b] = root_a
            if root_b:
                self.tree_map[root_a] = root_b
    def numberOfIslands(self):
        return self.count


'''
directed graph
'''
from collections import defaultdict
class DirectedGraph:
    def __init__(self, aj):
        ## if aj is already an adjacent list
        #self.adjacent_list = aj
        ## if aj is an array of paired edges
        self.adjacent_list = defaultdict(list)
        for item in aj:
            self.adjacent_list[item[0]].append(item[1])
        self.marked = {key:False for key in self.adjacent_list.keys()}
        self._canReach()

    def _canReach(self):
        for node in self.adjacent_list.keys():
            if not self.marked[node]:
                self.dfs(node,self.marked)

    def dfs(self,node,visited):
        visited[node] = True
        for neighbor in self.adjacent_list[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def canReach(self,node1,node2):
        visited = {node:False for node in self.adjacent_list.keys()}
        visited[node1] = True
        for neighbor in self.adjacent_list[node1]:
            if not visited[neighbor]:
                visited[neighbor] = True
                if self.dfs(neighbor,visited):
                    return True
                visited[neighbor] = False
        return False

'''
topological sort
'''
def topologicalSort(ajlist):
    visited = {key:0 for key in ajlist}
    res = []
    def dfs(node):
        visited[node] = 1
        for neighbor in ajlist.get(node,[]):
            if visited.get(neighbor,0) == 1:
                return False
            elif visited.get(neighbor,0) == 2:
                continue
            else:
                if not dfs(neighbor):
                    return False
        res.append(node)
        visited[node] = 2
        return True

    for node in ajlist.keys():
        if visited[node] == 0:
            if not dfs(node):
                return False
    res.reverse()
    return res






ajlist = {5:[2,0], 4:[0,1],2:[3], 3:[1]}
print topologicalSort(ajlist)
