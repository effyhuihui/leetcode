__author__ = 'effy'
'''
Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''





class Solution_dfs:
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


x = Solution_dfs()
print x.generateParenthesis(3)

class Solution_recursion:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if n == 0:
            return [""]
        res = []
        for j in range(n):
            left = self.generateParenthesis(j)
            right = self.generateParenthesis(n-1-j)
            for a in left:
                for b in right:
                    res.append('('+a+')'+b)
        return res
