__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
一个有效的IP地址由4个数字组成，每个数字在0-255之间。对于其中的2位数或3位数，不能以0开头
所以对于以s[i]开头的数字有3种可能：
1. s[i]
2. s[i : i+1]，s[i] !=0时
3. s[i : i+2]，s[i] != 0，且s[i : i+2] <= 255
'''
class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        res = []
        def dfs(path, remain):
            if remain == '':
                if len(path) == 4:
                    res.append('.'.join(path))
            else:
                if len(path) < 4:
                    for i in range(1,min(4,len(remain)+1)):
                        ## ensure even if the first char is 0, it will at least
                        ## have one round of recursion
                        if int(remain[:i]) <= 255:
                            dfs(path+[remain[:i]],remain[i:])
                        if int(remain[0]) == 0:
                            break
        dfs([],s)
        return res

x = Solution()
print x.restoreIpAddresses("0000")




