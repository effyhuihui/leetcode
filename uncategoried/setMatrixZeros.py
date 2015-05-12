__author__ = 'effy'
'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

thouhts:
iterate the whole matrix once, find the rows and cols to be set to zeros. then set them all in one take
'''
class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        if len(matrix) == 0:
            return
        m,n = len(matrix), len(matrix[0])
        row, col = {},{}
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        for key in row.keys():
            for i in range(n):
                matrix[key][i] = 0
        for key in col.keys():
            for i in range(m):
                matrix[i][key]= 0


