__author__ = 'effy'
'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or ..
A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
'''
class WordDictionary:
    def __init__(self):
        self.dict = {}
        self.lenDict = {}

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        self.dict[word] = True
        l = len(word)
        if l in self.lenDict:
            self.lenDict[l].add(word)
        else:
            self.lenDict[l] = set()
            self.lenDict[l].add(word)

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        l = len(word)
        if l not in self.lenDict:
            return False
        possible = list(self.lenDict[l])
        print possible
        if '.' not in word:
            return word in self.dict.keys()
        else:
            for i in possible:
                if self.matchDFS(word,i,0):
                    return True
            return False

    def matchDFS(self, word,cur,index):

        if index == len(word):
            return True
        if word[index] == '.' or word[index] == cur[index]:
            return self.matchDFS(word,cur, index+1)
        else:
            return False



# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("a")
wordDictionary.addWord("ab")
wordDictionary.addWord("mad")
print wordDictionary.search(".a")
#print wordDictionary.search("bad")
#print wordDictionary.search(".ad")
#print wordDictionary.search("b..")
'''
secondround
'''
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.isWord = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        level_parent = self.root
        for i in word:
            if i not in level_parent.children:
                node = TrieNode()
                level_parent.children[i] = node
            level_parent = level_parent.children[i]
        level_parent.isWord = True


    def search(self,word):
        parent = self.root
        for i in word:
            if i not in parent.children:
                return False
            else:
                parent = parent.children[i]
        return parent.isWord

    def startsWith(self,prefix):
        parent = self.root
        for i in prefix:
            if i in parent.children:
                parent = parent.children[i]
            else:
                return False
        return True