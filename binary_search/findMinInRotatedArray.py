__author__ = 'effy'
'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        n = len(num)
        start = 0
        end = n-1
        while start <= end:
            mid = (start+end)/2
            left = max(0, mid-1)
            right = min(n-1, mid+1)
            if num[mid] - num[left] <= 0 and num[mid] - num[right] <= 0:
                return num[mid]
            if num[mid] < num[end]:
                '''
                right side is with right increasing order
                '''
                end = mid - 1
            else:
                start = mid + 1



class Solution_secondround:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        l = len(nums)
        start, end = 0, l-1
        while start<=end:
            mid = (start+end)//2
            right,left = min(l-1,mid+1), max(0,mid-1)
            if nums[right]-nums[mid]>=0 and nums[left]-nums[mid]>=0:
                return nums[mid]
            if nums[mid] <= nums[end]:
                end = mid-1
            else:
                start = mid+1




a = Solution()
print a.findMin([2,1])
