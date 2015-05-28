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

but Time Limit Exceeded

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

class Solution_secondround:
    # @param height, a list of integer
    # @return an integer
    # @good solution!
    def largestRectangleArea(self, height):
        max_area = 0
        l = len(height)
        for i in range(l):
            left,right=i,i
            cur_height = height[i]
            while left>=0 and height[left]>=cur_height:
                left -= 1
            while right <l and height[right]>= cur_height:
                right += 1
            left += 1
            right -= 1
            local_max = (right-left+1)*cur_height
            max_area = max(local_max,max_area)
        return max_area


'''
http://www.cnblogs.com/zuoyuan/p/3783993.html
重点看图解
Actually, we can decrease the complexity by using stack to keep track of the height and
start indexes.
Compare the current height with previous one.

Case 1: current > previous (top of height stack)
Push current height and index as candidate rectangle start position.

Case 2: current = previous
Ignore.

Case 3: current < previous
keep popping out previous heights which is higher(stop until the prev height is the same or lower),
compute the candidate rectangle with height and width
(current index - previous index). Push the height and index to stacks.

建议用另外一个图来走一遍
(Note: it is better use another different example to walk through the steps, and you will understand it better).
'''
class Solution:
    # @param height, a list of integer
    # @return an integer
    # @good solution!
    def largestRectangleArea(self, height):
        maxArea = 0
        stackHeight = []
        stackIndex = []
        l = len(height)
        for i in range(l):
            if stackHeight == [] or height[i] > stackHeight[len(stackHeight)-1]:
                stackHeight.append(height[i])
                stackIndex.append(i)
            elif height[i] < stackHeight[len(stackHeight)-1]:
                lastIndex = None
                while stackHeight and height[i] < stackHeight[len(stackHeight)-1]:
                    lastIndex = stackIndex.pop()
                    tempArea = stackHeight.pop() * (i-lastIndex)
                    if maxArea < tempArea:
                        maxArea = tempArea
                stackHeight.append(height[i])
                stackIndex.append(lastIndex)
        while stackHeight:
            tempArea = stackHeight.pop() * (len(height) - stackIndex.pop())
            if tempArea > maxArea:
                maxArea = tempArea
        return maxArea

'''
my own way to solve it
'''
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