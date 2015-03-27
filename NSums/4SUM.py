# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)



解题思路：一开始想要像3Sum那样去解题，时间复杂度为O(N^3)，可无论怎么写都是Time Limited Exceeded。而同样的算法使用C++是可以通过的。
说明Python的执行速度比C++慢很多。还说明了一点，大概出题人的意思不是要让我们去像3Sum那样去解题，否则这道题就出的没有意义了。
这里参考了kitt的解法：http://chaoren.is-programmer.com/posts/45308.html

需要用到哈希表的思路，这样可以空间换时间，以增加空间复杂度的代价来降低时间复杂度。
先sort原数组，再建立一个字典lookup，字典的key值为数组中每两个元素的和，每个key对应的value为这两个元素的下标组成的元组，元组不一定是唯一的。
如对于num=[1,2,3,2]来说，dict={3:[(0,1),(0,3)], 4:[(0,2),(1,3)], 5:[(1,2),(2,3)]}。

这样就可以检查target-key这个值在不在dict的key值中，如果target-key在dict中并且下标符合要求，那么就找到了这样的一组解。由于需要去重，
这里选用set()类型的数据结构，即无序无重复元素集。最后将每个找出来的解(set()类型)转换成list类型输出即可。


http://www.cnblogs.com/zuoyuan/p/3699384.html
'''
class Solution_TLE:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        new_num = sorted(num)
        lookup = {}
        l = len(new_num)
        ## create a dict with key as any two num sum, and the value will be a list of tuples, tuples are indeices
        for i in range(l):
            for j in range(i+1,l):
                val = new_num[i]+new_num[j]
                lookup[val] = lookup.get(val, []) + [(i,j)]
        ## up until here they are the same
        ## below the set operation may cause the time limit exceeded.
        res_index = []
        for key in lookup.keys():
            left = target - key
            ## if there is a pair in lookup
            if left in lookup.keys():
                ## add all combinations from left and target, excluding those have duplicates
                res_index += [ tuple(sorted(i+j)) for i in lookup[key] for j in lookup[left] if len(set(i+j)) == 4]
                ## and remove same fours
                res_index = list(set(res_index))
        res = []
        for tup in res_index:
            res.append(tuple(new_num[i] for i in tup))
        return res

class Solution_other_ppl:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        l, res, lookup = len(num), set(), {}
        if l < 4: return []
        new_num = sorted(num)
        for i in range(l):
            for j in range(i+1, l):
                val = new_num[i]+new_num[j]
                lookup[val] = lookup.get(val, []) + [(i,j)]
        for i in range(l):
            for j in range(i+1, l-2):
                T = target-new_num[i]-new_num[j]
                if T in lookup:
                    for k in lookup[T]:
                        if k[0] > j: res.add((new_num[i],new_num[j],new_num[k[0]],new_num[k[1]]))
        return [list(i) for i in res]

x = Solution_TLE()
print x.fourSum([1, 0, -1, 0, -2, 2],0)