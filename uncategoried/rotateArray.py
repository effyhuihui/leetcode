__author__ = 'effy'
#-*- coding: utf-8 -*-
'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3,
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem.

hint： 看起来好多rotate的问题都可以转化成局部reverse的问题。

'''

'''
with extra space
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        l = len(nums)
        copy = [i for i in nums]
        new_index= l-k
        old_index = 0
        while old_index<l:
            if new_index>=l:
                new_index = 0
            nums[old_index] = copy[new_index]
            old_index += 1
            new_index += 1

x = Solution()
a = [1,2,3,4,5,6,7]
x.rotate(a,3)


'''
no extra space
以n - k为界，分别对数组的左右两边执行一次逆置；然后对整个数组执行逆置。
例如：n=7,k=3
[1,2,3,4,5,6,7]
先对[1,2,3,4] [5,6,7]分别reverse
[4,3,2,1,7,6,5]
再reverse整个list
[5,6,7,1,2,3,4]
'''
class Solution_opt:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        def reverse(start,end):
            mid = (start+end)//2
            i,j = start,end
            while i<=mid:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i+=1
                j-=1
        n = len(nums)
        k = k%n
        reverse(n-k,n-1)
        reverse(0,n-k-1)
        reverse(0,n-1)

x = Solution_opt()
a = [1,2,3,4,5,6]
x.rotate(a,11)


'''
将数组元素依次循环向右平移k个单位
'''
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        idx = 0
        distance = 0
        cur = nums[0]
        for x in range(n):
            next = (idx + k) % n
            temp = nums[next]
            nums[next] = cur
            idx = next
            cur = temp

            distance = (distance + k) % n
            if distance == 0:
                idx = (idx + 1) % n
                cur = nums[idx]
