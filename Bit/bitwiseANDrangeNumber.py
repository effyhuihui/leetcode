__author__ = 'effy'
'''
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.

http://bookshadow.com/weblog/2015/04/17/leetcode-bitwise-and-numbers-range/
'''
class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        i = 0
        while m != n:
            m = m >>1
            n = n >> 1
            i += 1
        return m << i