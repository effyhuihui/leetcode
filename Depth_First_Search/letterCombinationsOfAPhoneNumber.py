__author__ = 'effy'
'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.


Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        letter_map = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv",'9':"wxyz"}
        d = digits.replace("1",'')
        d = d.replace("0","")
        res = []
        def dfs(s,path):
            if s == '':
                res.append(path)
            else:
                for i in letter_map[s[0]]:
                    dfs(s[1:], path+i)
        if not d:
            return res
        else:
            dfs(d,'')
            return res

x = Solution()
print x.letterCombinations("23")
























