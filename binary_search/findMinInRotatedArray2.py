__author__ = 'effy'
'''
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        n = len(num)
        start = 0
        end = n-1
        mi = num[0]
        while start <= end:
            mid = (start+end)/2
            print num[start], num[mid], num[end]
            if num[mid] < num[end]:
                '''
                right side is with right increasing order
                '''
                mi = min(mi,num[mid])
                end = mid - 1
            elif num[mid] > num[end]:
                mi = min(mi, num[mid])
                start = mid + 1
            else:
                start += 1
            print start,end
a = Solution()
print a.findMin([3,1])

