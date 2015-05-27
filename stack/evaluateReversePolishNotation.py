__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
唯一一点需要注意的是在python中，是向下取整的。而这道题的oj是默认的c语言中的语法，所以需要在遇到'/'的时候注意一下。
'''
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i in "+-*/":
                a=int(stack.pop())
                b=int(stack.pop())
                if i == "+":
                    res = a+b
                elif i =="-":
                    res = b-a
                elif i == "/":
                    if a*b < 0:
                       res = -((-b)/a)
                    else:
                        res = b/a
                else:
                    res = a*b
                stack.append(res)
            else:
                stack.append(i)
        return int(stack[-1])


class Solution_secondround:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        num = []
        for cur in tokens:
            if cur in '+-*/':
                num1 = int(num.pop())
                num2 = int(num.pop())
                if cur == '+':
                    num.append(num1+num2)
                elif cur == '-':
                    num.append(num2-num1)
                elif cur == '*':
                    num.append(num1*num2*1.0)
                else:
                    if num1*num2 < 0:
                        num.append(-((-num2)/num1))
                    else:
                        num.append(num2/num1)
            else:
                num.append(cur)
        return int(num[-1])

a = Solution()
print a.evalRPN(["4", "13", "5", "/", "+"])