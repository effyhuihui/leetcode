__author__ = 'effy'
'''
Given an integer n, generate a square matrix filled with elements from 1 to n**2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

Thought: the implication is that the final matrix must be a n*n square
'''
class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        res = [ [None for i in range(n)] for j in range(n)]
        def fillCircle(start_coordinate, l,start_number):
            '''
            :param start_coordinate: the start coordinate of current circle, since it is a square, x,y is the same
            :param l:      length of the square circle
            :param start_number:  which number to start
            '''
            if l  == 1:
                res[n//2][n//2] = start_number
            else:
                start_m, start_n = start_coordinate, start_coordinate
                ## to right
                for i in range(l):
                    res[start_m][start_n+i] = start_number
                    start_number += 1
                ## to down
                for i in range(1,l):
                    res[start_m+i][start_n+l-1] = start_number
                    start_number += 1
                ## to left
                for i in range(1,l):
                    res[start_m+l-1][start_n+l-1-i] = start_number
                    start_number += 1
                ## to up
                for i in range(1,l-1):
                    res[start_m+l-1-i][start_n] = start_number
                    start_number+=1
        circle_l = n
        start_number = 1
        start_coordinate = 0
        while circle_l>0:
            fillCircle(start_coordinate,circle_l, start_number)
            start_number += circle_l*4-4
            circle_l -= 2
            start_coordinate += 1
        return res
x = Solution()
print x.generateMatrix(5)
