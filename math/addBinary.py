__author__ = 'effy'
'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''

class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        l1 ,l2 = len(a), len(b)
        i1,i2 = l1-1,l2-1
        carry = False
        global_sum = ''
        while i1 >= 0 and i2 >=0:
            if carry:
                local_sum = int(a[i1]) + int(b[i2]) +1
            else:
                local_sum = int(a[i1]) + int(b[i2])
            if local_sum//2:
                carry = True
            else:
                carry = False
            global_sum = str(local_sum%2)+global_sum
            i1 -= 1
            i2 -= 1
        while i1 >=0:
            if carry:
                local_sum = int(a[i1])+1
            else:
                local_sum = int(a[i1])
            if local_sum//2:
                carry = True
            else:
                carry = False
            global_sum = str(local_sum%2)+global_sum
            i1 -= 1
        while i2 >=0:
            if carry:
                local_sum = int(b[i2])+1
            else:
                local_sum = int(b[i2])
            if local_sum//2:
                carry = True
            else:
                carry = False
            global_sum = str(local_sum%2)+global_sum
            i2 -= 1
        if carry:
            global_sum = '1' + global_sum
        return global_sum


x = Solution()
print x.addBinary('0','0')



class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        result, carry, val, len_a, len_b, i = "", 0, 0, len(a), len(b), 0
        for i in range(max(len_a, len_b)):
            val = carry
            if i < len_a:
                val += int(a[len_a-i-1])
            if i < len_b:
                val += int(b[len_b-i-1])
            carry, val = val / 2, val % 2
            result = str(val)+result
        if carry == 1:
            result = "1" + result
        return result
x = Solution()
print x.addBinary('11','1')