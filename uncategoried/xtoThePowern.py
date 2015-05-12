__author__ = 'effy'
# -*- coding: utf-8

'''
Implement pow(x, n).
求幂函数的实现。使用递归，类似于二分的思路，解法来自Mark Allen Weiss的《数据结构与算法分析》
'''
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1.0
        elif n < 0:
            return 1 / self.pow(x, -n)
        elif n % 2:
            return self.pow(x*x,n/2)*x
        else:
            return self.pow(x*x,n/2)
x = Solution()
print x.myPow(1,9)
