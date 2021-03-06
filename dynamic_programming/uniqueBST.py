__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

'''
解题思路：这题从数学上讲，其实是卡特兰数。不过我们显然不从数学上来解决这个问题。这题是求二叉树的棵数。这里有个解题技巧：一般来说求数量，
要首先想到使用动态规划（dp），而如果是像下一题的要求，不只是数量，还要把所有的树都枚举出来，就要使用dfs（深度优先搜索）来遍历决策树了。

那么这道题是使用动态规划来解决的。那么如何去求这个问题的状态转移方程呢？其实大部分动态规划的难点都是求状态转移方程。n=0时，为空树，
那么dp[0]=1; n=1时，显然也是1，dp[1]=1；n=2时，dp[2]=2;
对于n>2时，一旦定下了root以后还剩下n-1个node可以分别分配在左右。（BST一旦tree structure定了，那么每个node的value只有一种分配方法）
所以状态方程是：
dp[n]=dp[0]*dp[n-1]+dp[1]*dp[n-2]+......+dp[n-1]*dp[0]；


'''

class Solution:
    # @return an integer
    def numTrees(self, n):
        dp = [1, 1, 2]
        if n <= 2:
            return dp[n]
        else:
            dp += [0 for i in range(n-2)]
            for i in range(3, n + 1):
                for j in range(1, i+1):
                    dp[i] += dp[j-1] * dp[i-j]
            return dp[n]

class Solution_secondround_dp:
    # @return an integer
    def numTrees(self, n):
        dp = [1,1,2]
        if n<=2:
            return dp[n]
        for i in range(3,n+1):
            current = 0
            for j in range(0,i):
                current += dp[j]*dp[i-1-j]
            dp.append(current)
        return dp[-1]


x = Solution()
print x.numTrees(3)









































