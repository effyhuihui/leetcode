__author__ = 'effy'
'''
given an array of strings, returns all groups of anagrams, All inputs are lower case
input : ["apple", "pleaa", "paer","pear","earp"]
return: [ ["apple", "pleaa", "paer"], ["pear","earp"] ]


thought:
sort each string by letters, and put into a hash map
'''

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        string_map = {}
        for i in strs:
            tmp = ''.join(sorted(i))
            string_map[tmp] = string_map.get(tmp,[]) + [i]
        res = []
        for i in string_map.keys():
            group = string_map[i]
            if len(group) > 1:
                res += group
        return res

x = Solution()
print x.anagrams(["apple", "plepa", "paer","pear","earp"])