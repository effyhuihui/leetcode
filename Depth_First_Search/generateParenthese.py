__author__ = 'effy'
'''
Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''




class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if n == 0:
            return ''
        res = []
        def dfs(path,stack,count):
            if count == n:
                if stack == []:
                    res.append(path)
                else:
                    stack.pop()
                    dfs(path+")", stack,count)
            else:
                dfs(path+"(", stack+["("],count+1)
                if stack != []:
                    stack.pop()
                    dfs(path+")",stack,count)

        dfs('',[],0)
        return res
x = Solution()
print x.generateParenthesis(3)