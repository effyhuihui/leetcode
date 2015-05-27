__author__ = 'effy'
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''
class Solution_secondround:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        stack = []
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if stack == []:
                    return False
                else:
                    match = stack.pop()
                    if (i == ')' and match == '(') or (i == ']' and match == '[') or (i=='}' and match =='{'):
                        pass
                    else:
                        return False
        if stack:
            return False
        return True