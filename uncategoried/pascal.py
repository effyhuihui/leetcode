__author__ = 'effy'
'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        res = [[1],[1,1]]
        for i in range(3,numRows+1):
            temp=[1 for j in range(i)]
            for j in range(1,i-1):
                print res[-1]
                temp[j] = res[-1][j]+ res[-1][j-1]
            res += [temp]
        return res

x = Solution()
print x.generate(5)


















