# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
https://oj.leetcode.com/problems/largest-rectangle-in-histogram/
For example,
Given height = [2,1,5,6,2,3],
return 10.
'''

'''
Thoughts:

Way 1:
就是从每一个bar往两边走，以自己的高度为标准，直到两边低于自己的高度为止，
然后用自己的高度乘以两边走的宽度得到矩阵面积。因为我们对于任意一个bar都计算了以自己为目标高度的最大矩阵，
所以最好的结果一定会被取到。每次往两边走的复杂度是O(n)，总共有n个bar，所以时间复杂度是O(n^2)
但是数据多的时候会time limit exceeded。


'''

class Solution1:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        n = len(height)
        max_sqft = 0
        for i in range(n):
            cur_height = height[i]
            left = max(0,i-1)
            right = min(n-1, i+1)
            while left>=0:
                if height[left]<cur_height:
                    break
                else:
                    left-=1
            left+=1
            while right < n:
                if height[right]<cur_height:
                    break
                else:
                    right+=1
            right-=1
            sqft = cur_height * (right-left+1)
            if sqft > max_sqft:
                max_sqft=sqft
        return max_sqft

'''
http://www.cnblogs.com/zuoyuan/p/3783993.html
最优的解法，我们create一个stack， stack里面存的是heights的index，
这个stack从下向上的index对应的高度是依次递增的（当然index本身也是递增的），
pop stack里的元素直到cur height大于stack的top。
为什么要pop呢，其实就是看在cur height之前，所能达到的最大高度以及这个最大高度跨越了多少范围，可以算出局部最优。

'''
class Solution2:
    # @param height, a list of integer
    # @return an integer
    # @good solution!
    def largestRectangleArea(self, height):
        maxArea = 0
        stackHeight = []
        stackIndex = []
        for i in range(len(height)):
            if stackHeight == [] or height[i] > stackHeight[len(stackHeight)-1]:
                stackHeight.append(height[i]); stackIndex.append(i)
            elif height[i] < stackHeight[len(stackHeight)-1]:
                lastIndex = 0
                while stackHeight and height[i] < stackHeight[len(stackHeight)-1]:
                    lastIndex = stackIndex.pop()
                    tempArea = stackHeight.pop() * (i-lastIndex)
                    if maxArea < tempArea: maxArea = tempArea
                stackHeight.append(height[i]); stackIndex.append(lastIndex)
        while stackHeight:
            tempArea = stackHeight.pop() * (len(height) - stackIndex.pop())
            if tempArea > maxArea:
                maxArea = tempArea
        return maxArea


class Solution3:
    # @param height, a list of integer
    # @return an integer
    # @good solution!
    def largestRectangleArea(self, height):
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

a = Solution1()
print a.largestRectangleArea([2,1,5,6,2,3])