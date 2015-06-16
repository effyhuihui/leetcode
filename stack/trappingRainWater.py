# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

这道题目的有趣之处在于，每一个当前elevation能储水的多少取决于它左右两边最高的min与它高度的差（有点像短板理论），
所以很显然，我们需要
这种方法是基于动态规划的，基本思路就是维护一个长度为n的数组，进行两次扫描，
一次从左往右，一次从右往左。第一次扫描的时候维护对于每一个bar左边最大的高度是多少，
存入数组对应元素中，第二次扫描的时候维护右边最大的高度，并且将左边和右边中较小的最大高度（我们成为瓶颈）
存入数组对应元素中。这样两遍扫描之后就可以得到每一个bar能承受的最大水量（将第二次扫描得到的高度减去当前bar的高度，若为
正，就说明能储存这么多高度的水），从而累加得出结果。
这个方法只需要两次扫描，所以时间复杂度是O(2*n)=O(n)。空间上需要一个长度为n的数组，复杂度是O(n)
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        from_left = [0]
        n = len(A)
        maximun = 0
        for i in range(1,n):
            maximun = max(maximun, A[i-1])
            from_left.append(maximun)
        maximun = 0
        total = 0
        for i in range(n-2,-1,-1):
            maximun = max(maximun,A[i+1])
            ## use max() in the outer level to avoid negative height
            total += max(0, (min(from_left[i], maximun) - A[i]))
        return total
'''
The previous solution is the optimization of the below one

'''
class Solution_secondround:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        l = len(A)
        left_highest = [0]
        for i in range(1,l):
            left_highest.append(max(left_highest[-1],A[i-1]))
        right_highest = [0]
        for i in range(l-2,-1,-1):
            right_highest.insert(0,max(right_highest[0],A[i+1]))
        total_water = 0
        #print left_highest, right_highest
        for i in range(l):
            min_bar = min(left_highest[i], right_highest[i])
            if min_bar>A[i]:
                local_water = 1*(min(left_highest[i],right_highest[i])-A[i])
                total_water += local_water
        return total_water


class Solution_3rd:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        l = len(A)
        total = 0
        left_highest = [0]
        right_highest = [0]
        for i in range(1,l):
            left_highest.append(max(A[i-1], left_highest[-1]))
        for i in range(l-2,-1,-1):
            right_highest.insert(0, max(A[i+1], right_highest[0]))
        for i in range(l):
            total += max(0, min(left_highest[i],right_highest[i])-A[i])
        return total

a = Solution()
print a.trap([0,1,0,2,1,0,1,3,2,1,2,1])
