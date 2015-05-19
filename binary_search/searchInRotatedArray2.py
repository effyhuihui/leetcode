__author__ = 'effy'
'''
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
'''
class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    '''
    if there is duplicates, only results in one more condition than non-duplicated
    rotated array to deal with,  that is :
    if A[mid] == A[end] (or A[mid] == A[start]), end-=1 (or start += 1)
    worst case time complexity could be linear
    '''
    def search(self, A, target):
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = (start+end)/2
            if A[mid] == target:
                return True
            if A[mid] < A[end]:
                '''
                it means the right side to mid is increasing and no rotation
                '''
                if A[mid] < target and target <= A[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            elif A[mid] > A[end]:
                '''
                means that the left side is increasing and no rotation
                '''
                if A[mid] > target and target >= A[start]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                ## if mid -- end, then we don't know which side are rotated,
                ## we can only move end/start one forward.
                end -= 1
        return False

class Solution_secondround:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):
        l = len(nums)
        start, end = 0, l-1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                return True
            ## right side is ordered and mid and end is not the same
            if nums[mid] < nums[end]:
                if target< nums[mid]:
                    end = mid -1
                else:
                    if nums[end] >= target:
                        start = mid+1
                    else:
                        end = mid -1
            ## left side is ordered and start / mid is not the same
            elif nums[mid] > nums[end]:
                if target > nums[mid]:
                    start  = mid +1
                else:
                    if target >= nums[start]:
                        end = mid -1
                    else:
                        start = mid + 1
            else:
                end  -= 1
        return False