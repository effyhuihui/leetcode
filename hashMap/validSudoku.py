__author__ = 'effy'
'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

example board: 	[".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
'''

'''
thought inverted index for both column and row
'''
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        ## isValid method: for each elements, it checks its row, column and 3 by 3 square
        def isValid(x, y, tmp):
            for i in range(9):
                if board[i][y]==tmp:
                    return False
            for i in range(9):
                if board[x][i]==tmp:
                    return False
            for i in range(3):
                for j in range(3):
                    if board[(x/3)*3+i][(y/3)*3+j]==tmp:
                        return False
            return True
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                tmp=board[i][j]
                board[i][j]='D' ## temporarily assign this to random character to avoid check on itself
                if not isValid(i,j,tmp):
                    return False
                else:
                    board[i][j]=tmp
        return True


class Solution2:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        # check for row
        for i in range(9):
            checked = [False]*9
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])-1
                    if checked[num]:
                        return False
                    else:
                        checked[num] = True

        # check for col
        for j in range(9):
            checked = [False]*9
            for i in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])-1
                    if checked[num]:
                        return False
                    else:
                        checked[num] = True

        # check for squares
        for j in range(0, 9, 3):
            for i in range(0, 9, 3):
                checked = [False]*9
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y] != '.':
                            num = int(board[i+x][j+y])-1
                            if checked[num]:
                                return False
                            else:
                                checked[num] = True

        return True

class Solution_second:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(9):
            word = {}
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in word:
                    return False
                else:
                    word[board[i][j]] = True
        for j in range(9):
            word = {}
            for i in range(9):
                if board[i][j] != '.' and board[i][j] in word:
                    return False
                else:
                    word[board[i][j]] = True

        for i in range(3):
            for j in range(3):
                word = {}
                for q in range(3):
                    for k in range(3):
                        if board[i*3+q][j*3+k] != '.' and board[i*3+q][j*3+k] in word:
                            return False
                        else:
                            word[board[i*3+q][j*3+k]] = True
        return True


class Solution_secondround:
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
                            if isValid(i,j) and self.solveSudoku(board):
                                return True
                            else:
                                board[i][j] = '.'
                        return False
            return True
        dfs(board)
        for i in range(9):
            board[i] = ''.join(board[i])


x = Solution()
x.isValidSudoku(	["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....",".15......",".....2...",".2.9.....","..4......"])