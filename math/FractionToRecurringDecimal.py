__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".


 0.16
6 ) 1.00
    0
    1 0       <-- Remainder=1, mark 1 as seen at position=0.
    - 6
      40      <-- Remainder=4, mark 4 as seen at position=1.
    - 36
       4      <-- Remainder=4 was seen before at position=1, so the fractional part which is 16 starts repeating at position=1 => 1(6).

解题的关键是当余数开始循环时，得数也会开始循环。

你需要用一个哈希表存储：key = 余数， value = 当前数位在小数得数中的位置。一旦找到重复的余数，就可以通过查找哈希表获得循环节的起点，
从而得到小数的循环节。

执行除法的过程中，余数可能变为0。此时说明小数是有限小数，可以立即返回得数。

与问题Divide Two Integers类似，需要注意负数和极限情况，例如-2147483648 / -1
'''
class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        negativeFlag = numerator * denominator < 0
        numerator = abs(numerator)
        denominator = abs(denominator)
        numList = []
        cnt = 0
        loopDict = {}
        loopStr = None
        while True:
            numList.append(str(numerator / denominator))
            cnt += 1
            numerator = 10 * (numerator % denominator)
            if numerator == 0:
                break
            loc = loopDict.get(numerator)
            if loc:
                loopStr = "".join(numList[loc:cnt])
                break
            loopDict[numerator] = cnt
        ans = numList[0]
        if len(numList) > 1:
            ans += "."
        if loopStr:
            ans += "".join(numList[1:len(numList) - len(loopStr)]) + "(" + loopStr + ")"
        else:
            ans += "".join(numList[1:])
        if negativeFlag:
            ans = "-" + ans
        return ans