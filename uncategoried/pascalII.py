__author__ = 'effy'
'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].
'''
class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        prev_row = [1,1]
        for i in range(2,rowIndex+1):
            new_row = [1 for k in range(i+1)]
            for j in range(1,i):
                new_row[j] = prev_row[j]+prev_row[j-1]
            prev_row = new_row[:]
        return prev_row
x = Solution()
print x.getRow(5)