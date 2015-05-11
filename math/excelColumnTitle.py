__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Given a positive integer, return its corresponding column title as appear
in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB

可以理解为进制转化，将10进制数转化为每位以A-Z表示的26进制数。

使用Python解题时，需要使用ord()函数将字母转化为整数，使用chr()函数将整数转化回字母。


'''


class Solution:
    # @return a string
    def convertToTitle(self, num):
        ans = ''
        while num:
            ans = chr(ord('A') + (num - 1) % 26) + ans
            num = (num - 1) / 26
        return ans

x = Solution()
print x.convertToTitle(52)
