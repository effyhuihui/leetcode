__author__ = 'effy'
'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.


'''
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        t_to_s = {}
        s_to_t = {}
        l = len(s)
        for i in range(l):
            t_to_s[t[i]] = t_to_s.get(t[i],s[i])
            s_to_t[s[i]] =s_to_t.get(s[i], t[i])
            replace = t_to_s[t[i]]
            replaced = s_to_t[s[i]]
            if replace != s[i] or replaced !=t[i]:
                return False
        return True

x = Solution()
print x.isIsomorphic("aa", "ab")  # should be False
print x.isIsomorphic("ab", "aa")  # should be False