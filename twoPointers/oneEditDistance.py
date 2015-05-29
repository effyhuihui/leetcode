__author__ = 'effy'
'''
# Given two strings S and T, determine if they are both one edit distance apart
simple and concise
'''

class Solution:
    # @param s, a string
    # @param t, a string
    # @return a boolean
    def isOneEditDistance(self, s, t):
        m, n = len(s), len(t)
        if m > n:
            return self.isOneEditDistance(t, s)
        if n - m > 1:
            return False

        i, shift = 0, n - m
        while i < m and s[i] == t[i]:
            i += 1
        '''
        if m == n, ignore the current different, move to the next char
        '''
        if shift == 0:
            i += 1
        '''
        else, stay the same, but pointer on t moved one ahead by adding 'shift'
        '''
        while i < m and s[i] == t[i + shift]:
            i += 1
        return i == m