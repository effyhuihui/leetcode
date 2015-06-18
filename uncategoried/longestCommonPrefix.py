__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Write a function to find the longest common prefix string amongst an array of strings.
超easy的呢：
1.首先遍历一遍整个list找出最短的string(min_l) （因为longest prefix不可能超过最短的长度）
2. sort一遍这个str list，这样的话第一个string和最后一个string是最最不同的
3. 对比第0个和最后一个str[0:min_len]， 找出这两个的common prefix即可
'''

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        min_l = 1000000
        strs.sort()
        for i in strs:
            if len(i) < min_l:
                min_l = len(i)
        if min_l == 0:
            return ''
        all_match = True
        print strs
        for i in range(min_l):
            print strs[0][:i+1], strs[-1]
            if strs[0][:i+1] == strs[-1][:i+1]:
                continue
            else:
                all_match = False
                break
        print all_match,i
        if all_match:
            return strs[0][:min_l]
        else:
            return strs[0][:i]


x = Solution()
print x.longestCommonPrefix(['a'])

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        longest = strs[0]
        for string in strs[1:]:
            i = 0
            while i < min(len(string), len(longest)) and string[i] == longest[i]:
                i += 1
            longest = longest[:i]
        return longest


