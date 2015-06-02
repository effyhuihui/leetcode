__author__ = 'effy'
'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''
'''
thinking is easy, but two points here is really really important
1. during recursive call, you need to make sure it returns from the inner most to the out
layer. if within search() you do not have if search():return True, then it will never return from
inside to outside. Need to have a way to pass the innder result out.

2. backtracking is needed here. within one recursive call(one dfs), we have one added matrix
however, if the recursive call returns and ends without True. you have to set everyting back
to False!!!!!!

'''
class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        if not board:
            return False
        m,n = len(board), len(board[0])
        ## added is a 2D matrix that record whether this char
        ## is already added in path
        added = [[False for i in range(n) ] for j in range(m)]
        exisitence = False
        def search(i,j,path):
            if path == word:
                return True
            ## the next char to be matched
            cur_match = word[len(path)]
            ## down
            if i-1>=0 and not added[i-1][j] and board[i-1][j] == cur_match:
                added[i-1][j] = True
                if search(i-1,j,path+cur_match):
                    return True
                added[i-1][j] = False
            ## up
            if i+1<m and not added[i+1][j] and board[i+1][j] == cur_match:
                added[i+1][j] = True
                if search(i+1,j,path+cur_match):
                    return True
                added[i+1][j] = False
            ## left
            if j-1>=0 and not added[i][j-1] and board[i][j-1] == cur_match:
                added[i][j-1] = True
                if search(i,j-1,path+cur_match):
                    return True
                added[i][j-1] = False
            ## right
            if j+1 < n and not added[i][j+1] and board[i][j+1] == cur_match:
                added[i][j+1] = True
                if search(i,j+1, path+cur_match):
                    return True
                added[i][j+1] = False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    added[i][j] = True
                    if search(i,j,word[0]):
                        return True
                    added[i][j] = False
        return False


class Solution_secondround:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        m,n=len(board),len(board[0])
        visited = [ [False for i in range(n)] for j in range(m)]
        def dfs(i,j,visited, word_par):
            if word_par == '':
                return True
            if (i < 0 or i >=m) or (j<0 or j>=n) or visited[i][j]:
                return False
            if board[i][j] == word_par[0]:
                visited[i][j] = True
                new_word = word_par[1:]
                if dfs(i-1,j,visited, new_word) or dfs(i+1,j,visited,new_word) or dfs(i,j-1,visited,new_word) or dfs(i,j+1,visited, new_word):
                    return True
                visited[i][j] = False
            return False
        for i in range(m):
            for j in range(n):
                if dfs(i,j,visited,word):
                    return True
        return False



x = Solution()
print x.exist(['aa'], 'aaa')