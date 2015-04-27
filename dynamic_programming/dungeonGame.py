__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon.
The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned
in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0
or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms;
other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if
he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
__________________
|-2 (K)	|-3  |	 3  |
|-5	    |-10 |     1  |
|10	    |30  |	-5 (P)|
-------------------
Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room
where the princess is imprisoned.
'''

'''
这里的DP是BOTTOM UP, 和minimum path sum不一样，这里需要考虑中间的结果。这里考虑的方法是从最后的结果出发（因为结果有一个已知的边界值）
dp[i][j]代表到目前这个格子为止血槽至少要多少才能走到最后一格
其转移方程为 dp[row][col]=max(1,min(dp[row+1][col],dp[row][col+1])-dungeon[row][col])  空间复杂度和时间复杂度都为 O(mn).
'''
class Solution_dp:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        grid = [[0 for i in range(n)] for j in range(m)]
        grid[-1][-1] = max(1,1-dungeon[-1][-1])
        for i in range(m-2,-1,-1):
            grid[i][n-1] = max(1,grid[i+1][n-1] - dungeon[i][n-1])
        for i in range(n-2,-1,-1):
            grid[m-1][i] = max(1,grid[m-1][i+1] - dungeon[m-1][i])
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                grid[i][j] = max(1,min(grid[i+1][j], grid[i][j+1]) - dungeon[i][j])
        return grid[0][0]

y = Solution_dp()
print y.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10, 30,-5]])


























