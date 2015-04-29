__author__ = 'effy'
'''
Write a function to find the longest common prefix string amongst an array of strings.
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


