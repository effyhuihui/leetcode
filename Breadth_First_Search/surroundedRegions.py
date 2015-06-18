__author__ = 'effy'
'''
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''
class Solution_dfs_recursion:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board:
            return board
        m,n = len(board),len(board[0])
        visited = [[False for i in range(n)] for j in range(m)]
        def dfs(i,j):
            if 0<=i<m and 0<=j<n and not visited[i][j] and board[i][j] == "O":
                visited[i][j] = True
                dfs(i,j-1)
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i+1,j)

        for i in range(m):
            if board[i][0] == "O":
                dfs(i,0)
            if board[i][n-1] == "O":
                dfs(i,n-1)
        for i in range(n):
            if board[0][i] == "O":
                dfs(0,i)
            if board[m-1][i] == "O":
                dfs(m-1,i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and not visited[i][j]:
                    board[i][j] = "X"



class Solution_stack:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board:
            return
        m,n = len(board), len(board[0])
        visited = [[False for i in range(n)] for j in range(m)]
        stack = []
        for i in range(m):
            if board[i][0] == "O":
                stack.append((i,0))
            if board[i][n-1] == "O":
                stack.append((i,n-1))
        for i in range(n):
            if board[0][i] == "O":
                stack.append((0,i))
            if board[m-1][i] == "O":
                stack.append((m-1,i))
        while stack:
            cur = stack.pop()
            i,j = cur[0],cur[1]
            if 0<=i<m and 0<=j<n and not visited[i][j] and board[i][j]=="O":
                visited[i][j] = True
                stack.append((i,j-1))
                stack.append((i,j+1))
                stack.append((i+1,j))
                stack.append((i-1,j))
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and board[i][j] == "O":
                    board[i][j] = "X"



class Solution_secondround:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        m, n = len(board), len(board[0])
        visited = [ [False for i in range(n)] for j in range(m)]
        def dfs(i,j):
            if 0<=i<m and 0<=j<n and not visited[i][j] and board[i][j] == 'O':
                visited[i][j]=True
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and board[i][j] == 'O':
                    board[i][j] = 'X'

x = Solution_secondround()
A = ["XXXX","XXXX","XXXX","XOXX"]
B =["X"]

c = [list(i) for i in a]
x = Solution_secondround()
print x.solve(c)

from collections import deque
class Solution_3rd:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        m, n = len(board), len(board[0])
        visited = [ [False for i in range(n)] for j in range(m)]
        components = deque()
        def valid(i,j):
            if i>=0 and i<m and j>=0 and j<n and not visited[i][j] and board[i][j] == 'O':
                visited[i][j] = True
                return True
            return False
        for i in range(m):
            if board[i][0] == 'O' and not visited[i][0]:
                visited[i][0] = True
                components.append((i,0))
            if board[i][n-1] == 'O' and not visited[i][n-1]:
                visited[i][n-1] = True
                components.append((i,n-1))
        for i in range(n):
            if board[0][i] == 'O' and not visited[0][i]:
                visited[0][i] = True
                components.append((0,i))
            if board[m-1][i] =='O' and not visited[m-1][i]:
                visited[m-1][i] = True
                components.append((m-1,i))
        while components:
                cur = components.popleft()
                p,q = cur[0], cur[1]
                if valid(p-1,q): components.append((p-1,q))
                if valid(p+1,q): components.append((p+1,q))
                if valid(p,q-1): components.append((p,q-1))
                if valid(p,q+1): components.append((p,q+1))
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'



