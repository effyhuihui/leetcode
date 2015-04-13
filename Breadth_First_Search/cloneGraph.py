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

'''
This is BFS
'''
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []

class Solution:
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


class Solution_bfs:
    # @param node, a undirected graph node
    # @return a undirected graph node
    # @BFS
    def cloneGraph(self, node):
        if node == None: return None
        queue = []; map = {}
        newhead = UndirectedGraphNode(node.label)
        queue.append(node)
        map[node] = newhead
        while queue:
            curr = queue.pop()
            for neighbor in curr.neighbors:
                if neighbor not in map:
                    copy = UndirectedGraphNode(neighbor.label)
                    map[curr].neighbors.append(copy)
                    map[neighbor] = copy
                    queue.append(neighbor)
                else:
                    # turn directed graph to undirected graph
                    map[curr].neighbors.append(map[neighbor])
        return newhead




















