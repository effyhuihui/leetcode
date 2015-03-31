__author__ = 'effy'
'''
implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

'''
class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        l = len(needle)
        if l > len(haystack):
            return -1
        for i in range(0,len(haystack)-l+1,1):
            print i, haystack[i:i+l]
            if haystack[i:i+l] == needle:
                return i
        return -1

x = Solution()
print x.strStr("mississippi", "issi")
print x.strStr("", "")