__author__ = 'effy'
'''

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code.
A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
'''


class Solution:
    # @return a list of integers
    def grayCode(self, n):
        res = []
        def dfs(path,num):
            if len(path) == n:
                res.append(num)
            else:
                for i in range(2):
                    dfs(path+str(i), num*2+i)
        dfs('',0)
        return res