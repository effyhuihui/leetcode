# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Given a string, find the length of the longest substring without repeating characters.
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
For "bbbbb" the longest substring is "b", with the length of 1.

Thought:
two pointers of index!!!!!  + a hash map with key of character, value of the last index it appears

解题思路：使用一个哈希表，记录字符的索引。例如对于字符串'zwxyabcabczbb'，当检测到第二个'a'时，由于之前已经有一个'a'了，
所以应该从第一个a的下一个字符重新开始测算长度，但是要把第一个a之前的字符在哈希表中对应的值清掉，如果不清掉的话，就会误以为还存在重复的。
比如检测到第二个'z'时，如果第一个'z'对应的哈希值还在，那就出错了，所以要把第一个'a'之前的字符的哈希值都重置才行。
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
x = Solution()
print x.lengthOfLongestSubstring("abcabcbb")
























