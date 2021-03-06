__author__ = 'effy'
'''
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
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
        node = self.root
        for letter in word:
            child = node.children.get(letter ,None)
            if child is None:
                child = TrieNode()
                node.children[letter] = child
            node = child
        node.isWord = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.root
        for letter in word:
            child = node.children.get(letter , None)
            if child is None:
                return False
            node = child
        return node.isWord

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.root
        for letter in prefix:
            child = node.children.get(letter, None)
            if child is None:
                return False
            node = child
        return True


# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")


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