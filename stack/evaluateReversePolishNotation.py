__author__ = 'effy'
'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        num = []
        for i in tokens:
            if i in "+-*/":
                a=int(num.pop())
                b=int(num.pop())
                if i == "+":
                    res = a+b
                elif i =="-":
                    res = b-a
                elif i == "/":
                    res = b/a
                else:
                    res = a*b
                num.append(res)
            else:
                num.append(i)
        return num[-1]
a = Solution()
print a.evalRPN(["4", "13", "5", "/", "+"])