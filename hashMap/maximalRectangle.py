# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
containing all ones and return its area.

解题思路：找出矩阵中最大的矩形，矩形中只包含1。这道题需要利用上一道题（Largest Rectangle in Histogram）的结论。比如对于以下矩阵。

　　　　　　　　0 0 0 0

　　　　　　　　0 0 1 0

　　　　　　　　0 1 1 0

　　　　　　　　1 0 1 1

　　　　　对于这个矩阵，对于每一行，我们按照上一道题的算法求解一遍，最后得出的就是最大的矩阵。
'''
class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        area = 0
        hist_len = [0]*len(matrix[0])
        l = len(matrix)
        for i in range(l):
            hist_len = [int(j)+int(k) if int(k)!=0 else 0 for j,k in zip(hist_len, matrix[i])]
            area = max(area, self.findLargestRectangleArea(hist_len))
        return area

    def findLargestRectangleArea(self, height):
        stack=[]; i=0; area=0
        while i<len(height):
            if stack==[] or height[i]>height[stack[len(stack)-1]]:
                stack.append(i)
            else:
                curr=stack.pop()
                width=i if stack==[] else i-stack[len(stack)-1]-1
                area=max(area,width*height[curr])
                i-=1
            i+=1
        while stack!=[]:
            curr=stack.pop()
            width=i if stack==[] else len(height)-stack[len(stack)-1]-1
            area=max(area,width*height[curr])
        return area
