__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
重点是reverse roman numerals
解题思路：将罗马数字转换成对应的整数。首先将罗马数字翻转，从小的开始累加，如果遇到CM（M-C=1000-100=900）这种该怎么办呢？因为翻转过来是MC，
M=1000先被累加，所以使用一个last变量，把M记录下来，如果下一个数小于M，那么减两次C，然后将C累加上，这个实现比较巧妙简洁。
'''
class Solution:
    # @return an integer
    def romanToInt(self, s):
        numerals = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1 }
        sum=0
        ## a[::-1] ----> reverse a string
        s=s[::-1]
        last=None
        for x in s:
            if last and numerals[x]<last:
                sum-=2*numerals[x]
            sum+=numerals[x]
            last=numerals[x]
        return sum
