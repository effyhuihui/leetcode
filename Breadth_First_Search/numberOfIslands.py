__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''
'''
给定一个由字符‘1’（陆地）和‘0’（水域）组成的二维网格地图，计算岛屿的个数。岛屿被水域环绕，由竖直或者水平方向邻接的陆地构成。
你可以假设网格地图的四条边都被水域包围。

测试样例见题目描述。

解题思路：
BFS
'''
class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        ## border cases
        if not grid:
            return 0
        m, n = len(grid),len(grid[0])
        if not m:
            return 0
        '''
        remember!!! do not use [[False]*n]*m
        This  reuses a list objects multiple times. [False]*n is used m times as reference
        This way, if you say grid[0][1], 1th element in all rows will be reassigned!!!!
        '''
        visited = [[False for i in range(n)] for i in range(m)]
        islands = 0
        ## this is to validate a (x,y) position
        def isValidPos(set):
            if set[0]<0 or set[0]>=m or set[1]<0 or set[1]>=n:
                return False
            return True
        ## this is to check all four cells atound current cell by BFS
        def bfs(i,j):
            queue = [(i,j)]
            while queue:
                cur = queue.pop()
                if  isValidPos(cur):
                    k,q = cur[0], cur[1]
                    if not visited[k][q] and grid[k][q]=='1':
                        queue+=[(k-1,q), (k+1,q), (k,q-1),(k,q+1)]
                    visited[k][q] = True

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    islands += 1
                    bfs(i,j)
        return islands

x = Solution()
a = ["11000",
     "11000",
     "00100",
     "00011"
     ]

print x.numIslands(["010","101","010"])


from collections import deque
class Solution_bfs_secondround:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        if not grid:
            return 0
        m,n = len(grid), len(grid[0])
        visited = [ [False for i in range(n)] for j in range(m)]
        islands = 0
        queue = deque()
        def valid(i,j):
            if 0<=i<m and 0<=j<n and grid[i][j] == '1' and not visited[i][j]:
                return True
            return False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    queue.append((i,j))
                    islands += 1
                    while queue:
                        cur = queue.popleft()
                        i,j = cur[0],cur[1]
                        visited[i][j] = True
                        if valid(i-1,j): queue.append((i-1,j))
                        if valid(i+1,j): queue.append((i+1,j))
                        if valid(i,j-1): queue.append((i,j-1))
                        if valid(i,j+1): queue.append((i,j+1))
        return islands

