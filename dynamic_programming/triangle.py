__author__ = 'effy'
'''
Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space,
where n is the total number of rows in the triangle.
'''
'''
dp[m][n] = min(dp[m-1][n-1], dp[m-1][n]) + dp[m][n]
'''
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        height = len(triangle)
        path_map = [[0]*(i+1) for i in range(height)]
        ## handle border case, including the top, two edges
        path_map[0][0] = triangle[0][0]
        for i in range(1,height):
            path_map[i][0] = triangle[i][0]+path_map[i-1][0]
            path_map[i][i] = triangle[i][i] + path_map[i-1][i-1]
        ## construct path map for the rest of triangle
        for i in range(1,height):
            current_edge = len(triangle[i])
            for j in range(1,current_edge-1):
                path_map[i][j] = triangle[i][j] + min(path_map[i-1][j-1], path_map[i-1][j])
        return min(path_map[height-1])


class Solution_secondround:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        dp = [i[:] for i in triangle]
        mintotal = 1000000
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                if j != 0 and j != len(triangle[i])-1:
                    dp[i][j] += min(dp[i-1][j], dp[i-1][j-1])
                elif j == 0:
                    dp[i][j] += dp[i-1][j]
                else:
                    dp[i][j] += dp[i-1][j-1]
        for i in dp[-1]:
            mintotal = min(i,mintotal)
        return mintotal


x = Solution()
a = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
x.minimumTotal(a)