__author__ = 'effy'
'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level
revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
'''
class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        if version1 == version2:
            return 0
        v1, v2 = [int(i) for i in version1.split('.')], [int(i) for i in version2.split('.')]
        l1, l2 = len(v1), len(v2)
        i1,i2 = 0,0
        while i1<l1 and i2<l2:
            if v1[i1]>v2[i2]:
                return 1
            elif int(v1[i1])< int(v2[i2]):
                return -1
            else:
                i1 += 1
                i2 += 1
        if (i1 == l1 and sum(v2[i2:]) == 0) or (i2 == l2 and sum(v1[i2:])==0):
            return 0
        elif i1 == l1 and i2<l2:
            return -1
        else:
            return 1
x = Solution()
print x.compareVersion('01','1.0')