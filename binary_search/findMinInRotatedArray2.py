__author__ = 'effy'
'''
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.

Catch: Duplicateion changes everything, it makes the time complexcity to be Liner
in the worst case.

Try to think of these cases:
[1,1,1,1,1,0], [0,1,1,1,1,1], [1,1,1,1,1]
[3,1,3]
[2,2,0,0,1,1]
'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        n = len(num)
        start = 0
        end = n-1
        mini = num[start]
        while start <= end:
            mid = (start+end)/2
            if num[mid] < mini:
                mini = num[mid]
            if num[mid] < num[end]:
                '''
                right side is with right increasing order
                '''
                end = mid - 1
            elif num[mid] > num[end]:
                start = mid + 1
            else:
                end -= 1
                if num[mid] == num[start]:
                    start += 1
        return mini

class Solution_secondround:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        l = len(num)
        start,end = 0, l-1
        mini = num[start]
        while start<=end:
            mid = (start+end)//2
            if num[mid]<mini:
                mini = num[mid]
            if num[mid] < num[end]:
                end = mid-1
            elif num[mid]> num[end]:
                start = mid+1
            else:
                if num[mid]==num[start]:
                    start += 1
                if num[mid] == num[end]:
                    end -= 1
        return mini



class Solution_3rd:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        mini = nums[0]
        l = len(nums)
        start, end = 0, l-1
        while start<=end:
            mid = (start+end)/2
            left, right = max(0,mid-1), min(l-1,mid+1)
            if nums[mid] < mini:
                mini = nums[mid]
            if nums[mid] - nums[left] < 0 and nums[mid] - nums[right] < 0:
                return nums[mid]
            if nums[mid] <= nums[end]:
                end -= 1
            else:
                start += 1
        return mini

a = Solution()
print a.findMin([])

