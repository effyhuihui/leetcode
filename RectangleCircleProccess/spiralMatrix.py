__author__ = 'effy'
# -*- coding: utf-8

'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
有一种方法哦，就是每次打印矩形的外面一圈，然后再打印里面一圈，一点点打印到最里面（一圈表示四边）
'''

class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        res = []
        if len(matrix) == 0:
            return res
        m,n = len(matrix),len(matrix[0])
        def printCircle(start_m,start_n,width,height):
            '''
            start_m, start_n represent the starting coordinate of the current circle
            width is the width of the circle, height is the height of the circle
            '''
            ##  --> right
            for k in range(width):
                res.append(matrix[start_m][start_n+k])
            ## --> down
            for k in range(1,height):
                res.append(matrix[start_m+k][start_n+width-1])
            ## --> left
            if height > 1:
                for k in range(1,width):
                    res.append(matrix[start_m+height-1][start_n+width-1-k])
            ## --> up
            if width > 1:
                for k in range(1,height-1):
                    res.append(matrix[start_m+height-1-k][start_n])
        start_m,start_n =0,0
        while m >0 and n>0:
            printCircle(start_m, start_n,n,m)
            start_m += 1
            start_n += 1
            m-=2
            n-=2
        return res
x = Solution()
print x.spiralOrder([[2,5,8],[4,0,-1]])
print x.spiralOrder([[2,3]])

print x.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])





