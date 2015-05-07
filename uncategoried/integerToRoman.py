__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

解题思路：整数（1~3999）到罗马数字的转换。字母前置表示减法，
例如CM表示M-C=1000-100=900，XL表示L-X=50-10=40。
'''
class Solution:
    # @return a string
    def intToRoman(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        list = ''
        for i in range(0, len(values)):
            while num >= values[i]:
                num -= values[i]
                list += numerals[i]
        return list