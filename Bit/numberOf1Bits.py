__author__ = 'effy'
# -*- coding:utf-8 -*-
'''
Write a function that takes an unsigned integer and returns the number of ’1' bits it has
(also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011,
so the function should return 3.
http://bookshadow.com/weblog/2015/03/10/leetcode-number-1-bits/
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans