__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order
(ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

哼！我自己也想到了的呢
输出字典序中的下一个排列。比如123生成的全排列是：123，132，213，231，312，321。那么321的next permutation是123。
下面这种算法据说是STL中的经典算法。在当前序列中，从尾端往前寻找两个相邻升序元素，升序元素对中的前一个标记为partition。
然后再从尾端寻找另一个大于partition的元素，并与partition指向的元素交换，然后将partition后的元素（不包括partition指向的元素）逆序排列。
比如14532，那么升序对为45，partition指向4，由于partition之后除了5没有比4大的数，所以45交换为54，即15432，
然后将partition之后的元素逆序排列，即432排列为234，则最后输出的next permutation为15234。确实很巧妙。
'''

class Solution:
    # @param num, a list of integer
    # @return nothing (void), do not return anything, modify num in-place instead.
    def nextPermutation(self, num):
        l = len(num)
        if l <= 1:
            return
        def swap(i,j):
            tmp = num[i]
            num[i] = num[j]
            num[j] = tmp
        ### 从后往前找，找到的第一个diff > 0的时候，会有:1.在i后面前部都是降序；2.i-1个元素比i小
        i = l-1
        while i>0:
            diff = num[i]-num[i-1]
            if diff > 0:
                ## 此时在i以及之后的数列中找到最小的、比i-1大的元素， swap
                for j in range(l-1,i-1,-1):
                    if num[j] > num[i-1]:
                        swap(i-1,j)
                        break
                break
            i -= 1
        ## 所以现在num[i-1]已经与num[i:]中第一个比num[i-1]大的元素互换了
        ## 以[5,4,7,5,3,2]为例子 现在得到的list是 [5,5,7,4,3,2]，仍然不是下一个permutation，为什么呢，因为swap了以后，
        ## 第一个最高位虽然是变了,但从i开始之后的元素仍然是降序，需要改成升序才能满足它是最小的笑一个permutation的属性
        # now swap for all element from current i to l-1
        t = i+l-1
        for k in range(i,(l+i)//2):
            swap(k,t-k)





x = Solution()
n = [2,5,4,3]
x.nextPermutation(n)
print n

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        k, l = -1, 0
        for i in xrange(len(num) - 1):
            if num[i] < num[i + 1]:
                k = i

        if k == -1:
            return num[::-1]

        for i in xrange(len(num)):
            if num[i] > num[k]:
                l = i

        num[k], num[l] = num[l], num[k]
        return num[:k + 1] + num[:k:-1]
