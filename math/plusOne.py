__author__ = 'effy'
'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''
class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        carry = 1
        l = len(digits)
        i = l-1
        while i >=0:
            if carry:
                local = digits[i] + 1
            else:
                local = digits[i]
            digits[i] = local%10
            carry = local//10
            i-=1
        if carry:
            digits.insert(0,1)
        return digits
