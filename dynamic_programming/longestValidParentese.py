__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed)
parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''
class Solution_brutal_force:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        def count(s):
            stack = []
            count = 0
            l = len(s)
            for i in range(l):
                if s[i] == "(":
                    stack.append(s[i])
                else:
                    if stack == []:
                        break
                    else:
                        stack.pop()
                        count += 1
            return count
        longest = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                c = count(s[i:j])
                longest = max(longest,c)
        return longest*2
x = Solution_brutal_force()
#print x.longestValidParentheses(")()())")

'''
用一个stack来maintain左括号的index（这个stack的作用和判断valid parentese是一样的） 每次遇到右括号就pop左括号的index
在遍历括号array的时候会有两种情况出现：
1. 左括号的个数比右括号的多 ---> pop完了以后还有左括号的index在stack里
2. 右括号的个数比左括号的多   ---> 要pop的时候将会面对一个空的stack

'''

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        maxlen = 0
        stack = []
        start = -1
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)     # push the INDEX into the stack!!!!
            else:
                if stack == []:
                    ## discard the previous array, not valid until here, start a new sub array from here
                    start = i
                else:
                    stack.pop()
                    if stack == []:
                        maxlen = max(maxlen, i-start)
                    else:
                        ## if there is still left parenthese in stack, after pop, the index left inside is the
                        ## previous (, the current extra left (
                        maxlen = max(maxlen, i-stack[-1])
        return maxlen


x = Solution()
print x.longestValidParentheses("()()")
