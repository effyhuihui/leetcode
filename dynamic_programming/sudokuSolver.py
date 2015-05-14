__author__ = 'effy'
'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''
'''
dfs!!!!!!
'''
class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        for i in range(9):
            board[i] = list(board[i])
        def isValid(x,y):
            tmp = board[x][y]
            #check for col
            for i in range(9):
                if i != x and board[i][y] == tmp:
                    return False
            ## check for rows
            for i in range(9):
                if i != y and board[x][i] == tmp:
                    return False
            ## check for 3*3 board
            box_i,box_j = x//3, y//3
            for i in range(box_i*3, box_i*3+3):
                for j in range(box_j*3, box_j*3+3):
                    if i !=x and j !=y and board[i][j] == tmp:
                        return False
            ## all test passes
            return True
        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in '123456789':
                            board[i][j] = num
                            if isValid(i,j) and dfs(board):
                                ## the existed board  with board[i][j] = num goes all the way through!
                                return True
                            board[i][j] = '.'
                        ## all 1-9 in the current cell is not valid, goes one level up, backtracking to the previous
                        ## cell
                        return False
            ## if it stick through all loop, it is a pass
            return True
        dfs(board)
        for i in range(9):
            board[i] = ''.join(board[i])












