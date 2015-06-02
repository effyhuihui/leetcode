__author__ = 'effy'
'''
Given a 2D board and a list of words from the dictionary, find all words in the board.


Each word must be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
'''
class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self,word):
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.isWord = True

class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        m,n = len(board), len(board[0])
        visited = [ [False for i in range(n)] for j in range(m)]
        root = Trie()
        for word in words:
            root.addWord(word)
        res = set()
        def search(trienode, i,j, visited, path):
            if not trienode or (i<0 or i >=m) or (j<0 or j>=n) or visited[i][j]:
                return
            if board[i][j] not in trienode.children:
                return
            next_trienode = trienode.children[board[i][j]]
            next_path = path+[board[i][j]]
            if next_trienode.isWord:
                res.add(''.join(next_path))
            visited[i][j] = True
            search(next_trienode,i-1,j, visited, next_path)
            search(next_trienode, i+1,j, visited, next_path)
            search(next_trienode, i,j-1, visited,next_path)
            search(next_trienode, i, j+1, visited, next_path)
            visited[i][j] = False
            next_path.pop()
        for i in range(m):
            for j in range(n):
                search(root.root,i,j,visited,[])
        return list(res)

x = Solution()
print x.findWords([['a'],['a']], 'a')


