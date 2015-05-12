__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

不许用乘、除和求余实现两数的相除。那就只能用加和减了。正常思路是被除数一个一个的减除数，直到剩下的数比除数小为止，就得到了结果。
这样是无法ac的，因为时间复杂度为O(n)，比如一个很大的数除1，就很慢。这里我们可以用二分查找的思路，可以说又是二分查找的变种。
'''

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        max_int = 2147483648
        a = abs(dividend)
        b = abs(divisor)
        if a < b:
            return 0
        sum, count, res = 0,0,0
        while a >= b:
            sum = b
            count = 1
            while sum + sum <= a:
                sum += sum
                count += count
            a -= sum
            res += count
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = 0 - res
        ## overflow handling
        if res == max_int:
            return res-1
        elif res == -max_int:
            return res
        #####################
        return res
