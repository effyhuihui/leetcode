# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Given a string, find the length of the longest substring without repeating characters.
For example, the longest substring without repeating letters for "abcabcbb" is "abc",
which the length is 3.
For "bbbbb" the longest substring is "b", with the length of 1.

Thought:
two pointers of index!!!!!  + a hash map with key of character, value of the last index it appears

'''

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = 0
        maxlen = 0
        l = len(s)
        index_map = {}
        for i in range(l):
            last_seen = index_map.get(s[i], -1)
            ## it appeared already, then the new start should set to be last_seen + 1
            if last_seen != -1:
                ## reset back all characters appearance before the new start  to -1
                while start <= last_seen:
                    index_map[s[start]] = -1
                    start += 1
                ## now start = last_seen + 1
            maxlen = max(i-start+1, maxlen)
            index_map[s[i]] = i
        return maxlen

class Solution_secondround:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = 0
        maxlen = 0
        l = len(s)
        index_map = {}
        for i in range(l):
            cur_char = s[i]
            last_seen = index_map.get(cur_char,-1)
            ## if last seen is within i and start, set start to last_seen+1
            if last_seen >= start:
                start = last_seen +1
            else:
                maxlen = max(maxlen,i-start+1)
            index_map[cur_char] = i
        return maxlen



x = Solution()
print x.lengthOfLongestSubstring("abcabcbb")
























