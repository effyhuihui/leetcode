# -*- coding: utf-8 -*-
def merge(A, m, B, n):
	'''
	Given two sorted integer arrays A and B, merge B into A as one sorted array.

	Note:
	You may assume that A has enough space (size that is greater or equal to m + n) 
	to hold additional elements from B. The number of elements initialized in A and 
	B are m and n respectively.

	Catch:
	The catch here is to manage the operation in O(M+N) time, since "insert" will 
	take O(M*N) time, and to make the merge IN PLACE.

	Thoughts:
	其实很简单，要避免insert的话，一般就是从后往前进行插入。 这里既然A已经是一个很大的array了，
	而且B和A的occupied的长度都知道（分别是m，n），那么最后merge完以后的array长度也就是已知的m+n。
	所以只需要把AB的current last element来进行比较，把其中较大的放到A列的current末尾即可。 要是两个数列
	不是同时sort完，再把最后剩下的数组的的0 到 current last 的所有元素依次放入A数组的0：current last即可。

	注意：
	1. 这里所有带有“current”的变量都是需要maintain的。
	2. 其实就是不停的在replace A数组的第N个元素，直到其中一个数组终结。
	'''
	# compare from the end element of the two arraies
	pos_b, pos_a = n, m
	## cur starts at the end of the future sorted array
	cur = m+n- 1
	while pos_b and pos_a:
		if A[pos_a-1] >= B[pos_b-1]:
			A[cur] = A[pos_a-1]
			pos_a -= 1
		else:
			A[cur] = B[pos_b-1]
			pos_b -= 1
		cur -= 1
	if pos_b:
		A[:cur+1] = B[:cur+1]
	return A[:m+n]


class Solution_secondround:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        nums1 += [0 for i in range(n)]
        cur1, cur2 = m-1, n-1
        curnew = m+n-1
        while cur1 >=0 and cur2 >=0:
            if nums1[cur1] >= nums2[cur2]:
                nums1[curnew] = nums1[cur1]
                cur1 -= 1
            else:
                nums1[curnew] = nums2[cur2]
                cur2 -= 1
            curnew -= 1
        while cur2>=0:
            nums1[:curnew+1] = nums2[:cur2+1]
        return nums1




A = [1,5,7,9,11, 0,0,0,0,0,0,0,0,0]
B = [2,4,7,9,12,14]

x = merge(A, 5, B, 6)
print x
