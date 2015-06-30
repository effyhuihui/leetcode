__author__ = 'effy'
'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
'''

class Solution_dfs:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m,n = len(matrix), len(matrix[0])
        def validIndex(i,j):
            if i >=0 and i< m and j>=0 and j<n:
                return True
        def dfs(i,j):
            if validIndex(i,j+1) and validIndex(i+1,j) and validIndex(i+1,j+1) \
                and matrix[i][j+1] == '1' and matrix[i+1][j] == '1' and matrix[i+1][j+1] == '1':
                return min(dfs(i+1,j+1),dfs(i+1,j), dfs(i,j+1))+1
            return 0
        max_square = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    edge = 1 + dfs(i,j)
                    max_square = max(edge*edge, max_square)
        return max_square

x = Solution_dfs()
#print x.maximalSquare([['1','0','1','0','0'],['1', '0', '1', '1', '1'],
#                       ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']])

a= ["0001","1101","1111","0111","0111"]
b = [list(i) for i in a]
#print x.maximalSquare(b)

class Solution_dp:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m,n = len(matrix),len(matrix[0])
        if '1' in matrix:
            max_square = 1
        else:
            max_square = 0
        dp_edge = [[int(matrix[i][j]) for j in range(n)] for i in range(m) ]
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if matrix[i][j] == '1':
                    dp_edge[i][j] = min(dp_edge[i+1][j], dp_edge[i][j+1], dp_edge[i+1][j+1])+1
                    max_square = max(dp_edge[i][j]**2, max_square)
        return max_square

x = Solution_dp()
print x.maximalSquare([['1','0','1','0','0'],['1', '0', '1', '1', '1'],
                       ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']])

a= ["0001","1101","1111","0111","0111"]
b = [list(i) for i in a]
print x.maximalSquare(b)
print x.maximalSquare(['1'])
