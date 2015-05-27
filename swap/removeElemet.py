__author__ = 'effy'
'''
Given an array and a value, remove all instances of that value in place and return the
new length.

The order of elements can be changed.
It doesn't matter what you leave beyond the new length.
'''

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        l = len(A)
        if l == 0 :
            return l
        count = 0
        for i in range(l):
            if A[i] == elem:
                count += 1
            else:
                ## move all non-elem to the end of the list
                A[i-count] = A[i]
        return l-count

class Solution_secondround:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        count = 0
        for i in range(len(A)):
            if A[i] == elem:
                count += 1
            else:
                A[i-count] = A[i]
        print A
        return len(A) - count

x = Solution()
print x.removeElement([1,1,1,2],1)

