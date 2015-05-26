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


class Solution_secondround:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        word_dict = {}
        res = []
        for i in strs:
            s = ''.join(sorted(i))
            word_dict[s] = word_dict.get(s, []) + [i]
        for i in word_dict.keys():
            if len(word_dict[i]) >=2:
                res+=word_dict[i]
        return res


x = Solution()
print x.anagrams(['',''])
print x.anagrams(["apple", "plepa", "paer","pear","earp"])