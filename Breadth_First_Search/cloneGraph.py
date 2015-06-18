__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Clone an undirected graph. Each node in the graph contains a label and a list of its
neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

'''


class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
'''
This is BFS
思路是：
1.先copy一个node，只需要label即可，并把original node 放入nodes_queue。再update nodes_copied map
所以可以保证queue里面的所有node都已经有了一个copy
2.pop出queue里面一个node, 处理它的neighbors， neighbor 要么是已经create了，要么没有，所以针对两个情况分别处理

以上。
undirected graph的表示方式很有意思，以{0,1,2#1,2#2,2}为例，0与1，2为邻，因为0和1关系已经出现过一次，所以在1的时候，0不作为neighbor
点出现，这样就避免了重复。每一pair都只出现了一次：）
'''
class Solution_bfs:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None:
            return None
        nodes_queue = [node]
        newhead = UndirectedGraphNode(node.label)
        nodes_copied = {node:newhead}
        ## only add copied node into nodes_stack
        while nodes_queue:
            cur = nodes_queue.pop()
            for i in cur.neighbors:
                if i not in nodes_copied:
                    n = UndirectedGraphNode(i.label)
                    nodes_copied[i]=n
                    nodes_queue.append(i)
                nodes_copied[cur].neighbors.append(nodes_copied[i])
        return newhead


'''
map的作用在于替代bfs和dfs中的visit数组，一旦map中出现了映射关系，就说明已经复制完成，也就是已经访问过了。
'''
class Solution_dfs:
    # @param node, a undirected graph node
    # @return a undirected graph node
    # @BFS
    def cloneGraph(self, node):
        def dfs(input, map):
            if input in map:
                return map[input]
            output = UndirectedGraphNode(input.label)
            map[input] = output
            for neighbor in input.neighbors:
                output.neighbors.append(dfs(neighbor, map))
            return output
        if node == None: return None
        return dfs(node, {})




from collections import deque
class Solution_secondround:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        cloned = {}
        if not node:
            return None
        new_head = UndirectedGraphNode(node.label)
        cloned[node] = new_head
        queue = deque()
        queue.append(node)
        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = UndirectedGraphNode(neighbor.label)
                    queue.append(neighbor)
                cloned[cur].neighbors.append(cloned[neighbor])
        return new_head

from collections import deque
class Solution_3rd:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        clone_node = UndirectedGraphNode(node.label)
        clone_map = {node:clone_node}
        processing = deque()
        processing.append(node)
        while processing:
            cur = processing.popleft()
            copy = clone_map[cur]
            for neighbor in cur.neighbors:
                if neighbor not in clone_map:
                    new = UndirectedGraphNode(neighbor.label)
                    clone_map[neighbor] = new
                    processing.append(neighbor)
                copy.neighbors.append(clone_map[neighbor])
        return clone_map[node]
















