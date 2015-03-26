__author__ = 'effy'
'''
iven an array of integers, every element appears twice except for one.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
'''
'''
hash map solution, with extra memory
'''
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        lookup = {}
        for i in A:
            lookup[i] = lookup.get(i,0)+1
        for i in A:
            if lookup[i] == 1:
                return i
'''
bit manipulation, xor, no extra mem
'''
class Solution2:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ans = A[0]
        for i in range(1,len(A)):
            ans = ans ^ A[i]
        return ans
