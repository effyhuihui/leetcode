__author__ = 'effy'
# -*-coding: utf-8 -*-
'''
Given two words (beginWord and endWord), and a dictionary, find the length of shortest transformation sequence
from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
'''
'''
使用BFS, 单词和length一块记录, dict中每个单词只能用一次, 所以用过即删。dict给的是set类型,
检查一个单词在不在其中(word in dict)为O(1)时间。设单词长度为L, dict里有N个单词,
每次扫一遍dict判断每个单词是否与当前单词只差一个字母的时间复杂度是O(N*L), 而每次变换当前单词的一个字母,
看变换出的词是否在dict中的时间复杂度是O(26*L), 所以要选择后者。
'''

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string!!!dict is a set type!!!
    # @return an integer
    def oneLevelSeparation(self,a,b):
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1
                if diff >= 2:
                    return False
            return True
    def ladderLength(self, beginWord, endWord, wordDict):
        wordDict = list(wordDict)
        wordDict.append(endWord)
        word_list = [beginWord]
        level = 1
        while word_list:
            cur_word = word_list.pop(0)
            for i in wordDict:
                if self.oneLevelSeparation(i, cur_word):
                    if i == endWord:
                        return level
                    word_list.append(i)
                    wordDict.remove(i)
            level += 1
        return 0

x = Solution()
print x.oneLevelSeparation('hit','cog')
print x.ladderLength('hit','cog',["hot","dot","dog","lot","log"])








