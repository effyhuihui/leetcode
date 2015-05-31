__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
'''
class Solution_recursion:
    # @param s1, a string
    # @param s2, a string
    # @return a boolean
    def isScramble(self, s1, s2):
        l1,l2 = len(s1), len(s2)
        if l1 != l2:
            return False
        ## 为了减少时间，需要剪枝。。。在charlist不同的情况下直接排除，
        char1, char2 = sorted(list(s1)), sorted(list(s2))
        if char1 != char2:
            return False
        if s1 == s2:
            return True
        else:
            for i in range(1,l1):
                if (self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:], s2[i:])) \
                    or (self.isScramble(s1[:i], s2[l2-i:]) and self.isScramble(s1[i:],s2[:l2-i])):
                    return True
        return False
'''
使用了一个三维数组boolean result[len][len][len],其中第一维为子串的长度，第二维为s1的起始索引，第三维为s2的起始索引。
result[k][i][j]表示s1[i...i+k]是否是s2[j...j+k]的scramble string。
'''


class Solution:
    # @param s1, a string
    # @param s2, a string
    # @return a boolean
    def isScramble(self, s1, s2):
        l1, l2 = len(s1), len(s2)
        if l1 != l2:
            return False
        char1 ,char2 = sorted(list(s1)), sorted(list(s2))
        if char1 != char2:
            return False
        dp = [[[0 for k in range(l1)] for j in range(l1)] for i in range(l1+1)]
        ## 边界条件， 当length = 0的时候 所有的组合都是对方的scramble string
        for i in range(l1):
            for j in range(l2):
                dp[0][i][j] = True

        ## to search for all possible length of sub string from 1 to length
        for i in range(1,l1):
            ## search through all possible starting position for s1 given length i
            for j in range(0,l1-i+1):
                ## search through all possible starting position for s2 given length i
                for k in range(0,l2-i+1):
                    if dp[i][j][k] == 0:
                        dp[i][j][k] = s1[j:j+i] == s2[k:k+i]



class Solution_recursion_secondround:
    # @param s1, a string
    # @param s2, a string
    # @return a boolean
    def isScramble(self, s1, s2):
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        charlist1, charlist2 = sorted(list(s1)), sorted(list(s2))
        if charlist1 != charlist2:
            return False
        for i in (1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]))\
                    or (self.isScramble(s1[:i], s2[len(s2)-i:]) and self.isScramble(s1[i:], s2[:len(s2)-i])):
                return True
        return False

x = Solution_recursion()
print x.isScramble("abcdefghijklmnopq", "efghijklmnopqcadb")