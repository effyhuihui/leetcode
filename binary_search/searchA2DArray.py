__author__ = 'effy'
'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following
properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''
class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        ## start, end are indices of arrays
        start = 0
        end = len(matrix)-1
        ##s,e are indices of integers inside arrays
        s = 0
        n = len(matrix[0])
        e = n - 1
        while start <= end and s<=e:
            mid = (start+end)/2
            m = (s+e)/2
            print "middles",mid, m
            if matrix[mid][m] == target:
                return True
            if matrix[mid][m] > target:
                if target >= matrix[mid][0]:
                    e = m - 1
                else:
                    end = mid - 1
                    s = 0
                    e = n-1
            else:
                if target <= matrix[mid][e]:
                    s = m + 1
                else:
                    print 'in'
                    s = 0
                    e = n-1
                    start = mid + 1
        return False
'''
Other thoughts:

we can also use 0~m*n as index and convert them into [m,n] and then
access element inside the 2D array
'''
class Solution2:
    '''
    This works exactly like an flatten array
    '''
    def searchMatrix(self, matrix, target):
        ## there are in total n elements in the 2D array
        n = len(matrix)*len(matrix[0])
        l = len(matrix[0])
        def index_conversion(index):
            x = index/l
            y = index - x*l
            return x, y
        start = 0
        end = n-1
        while start <= end:
            mid = (start+end)/2
            x,y = index_conversion(mid)
            current = matrix[x][y]
            if current == target:
                return True
            elif current < target:
                start = mid+1
            else:
                end = mid-1
        return False


a = Solution2()
print a.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 4)
