# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Given an array of size n, find the majority element. The majority element is the
element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist
in the array.
'''

'''
way 1 : hash table
'''
def majorityElement(num):
    d = {}
    # res stores a tuple (actual value, times appeared), to maintain the current majority element
    res = (None, 0)
    for i in num:
        d[i] = d.get(i, 0) + 1
        if d[i] > res[1]:
            res = (i, d[i])
    return res[0]
'''
way 2: Moore voting --> applies to finding the element that appears more than half in an array
“投票算法”，设定两个变量candidate和count。candidate保存当前可能的候选众数，count保存该候选众数的出现次数。

遍历数组num。

如果当前的数字e与候选众数candidate相同，则将计数count + 1

否则，如果当前的候选众数candidate为空，或者count为0，则将候选众数candidate的值置为e，并将计数count置为1。

否则，将计数count - 1

最终留下的候选众数candidate即为最终答案。

以上算法时间复杂度为O(n)，空间复杂度为O(1)

'''
def majorityElement(num):
    majority, count = None, 0
    for i in num:
        if count == 0:
            majority = i
            count += 1
        elif i == majority:
            count += 1
        else:
            count -= 1
num = [1,1,1,1,1,1,2,2,0]
a = majorityElement(num)
print a