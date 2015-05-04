__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate
a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

这类型问题统称为递归回溯问题，也可以叫做对决策树的深度优先搜索（dfs）。
N皇后问题有个技巧的关键在于棋盘的表示方法，这里使用一个数组就可以表达了。
比如board=[1, 3, 0, 2]，这是4皇后问题的一个解，意思是：在第0行，皇后放在第1列；在第1行，皇后放在第3列；
在第2行，皇后放在第0列；在第3行，皇后放在第2列。
这道题提供一个递归解法，下道题使用非递归。check函数用来检查在第k行，皇后是否可以放置在第j列。
'''
class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        res = []
        def check(k,j,path):
            ## check whether in kth row, queen can be filed in jth spot
            for i in range(k):
                if path[i] == j or abs(k-i)==abs(path[i]-j):
                    return False
            return True
        def dfs(path):
            l = len(path)
            if l == n:
                res.append(path)
            else:
                for i in range(n):
                    if check(l,i,path):
                        dfs(path+[i])
        dfs([])
        final = []
        for i in res:
            final.append([])
            for j in i:
                final[-1]+=['.'*j+'Q'+'.'*(n-1-j)]
        return final



x = Solution()
print x.solveNQueens(4)


