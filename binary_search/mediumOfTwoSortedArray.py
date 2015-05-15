__author__ = 'effy'
#-*- coding: utf-8 -*-
'''
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
'''
'''
Method 2 (By comparing the medians of two arrays)
This method works by first getting medians of the two sorted arrays and then comparing them.

Let ar1 and ar2 be the input arrays.

Algorithm (if ar1 and ar2 are of same length):

1) Calculate the medians m1 and m2 of the input arrays ar1[]
   and ar2[] respectively.
2) If m1 and m2 both are equal then we are done.
     return m1 (or m2)
3) If m1 is greater than m2, then median is present in one
   of the below two subarrays.
    a)  From first element of ar1 to m1 (ar1[0...|_n/2_|])
    b)  From m2 to last element of ar2  (ar2[|_n/2_|...n-1])
4) If m2 is greater than m1, then median is present in one
   of the below two subarrays.
   a)  From m1 to last element of ar1  (ar1[|_n/2_|...n-1])
   b)  From first element of ar2 to m2 (ar2[0...|_n/2_|])
5) Repeat the above process until size of both the subarrays
   becomes 2.
6) If size of the two arrays is 2 then use below formula to get
  the median.
    Median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1]))/2


首先我们来看如何找到两个数列的第k小个数，即程序中getKth(A, B , k)函数的实现。
用一个例子来说明这个问题：A = {1，3，5，7}；B = {2，4，6，8，9，10}；
如果要求第7个小的数，A数列的元素个数为4，B数列的元素个数为6；k/2 = 7/2 = 3，而A中的第3个数A[2]=5；
B中的第4个数B[3]=6；而A[2]<B[3]；则A[0]，A[1]，A[2]中必然不可能有第7个小的数。因为A[2]<B[3]，
所以比A[2]小的数最多可能为A[0], A[1], B[0], B[1], B[2]这5个数，也就是说A[2]最多可能是第6个大的数，
由于我们要求的是getKth(A, B, 7)；现在就变成了求getKth(A', B, 4)；即A' = {7}；
B不变，求这两个数列的第4个小的数，因为A[0]，A[1]，A[2]中没有解，所以我们直接删掉它们就可以了。这个可以使用递归来实现。
'''
'''
O(log(m+n))
'''
class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findKthSmallest(self,A,B, k):
        '''
        :param A: a list of numbers, with length l1
        :param B: a list of numbers, with length l2 (l1<l2)
        :param k: Kth smallest number to be found
        :return: the kth smallest number
        '''
        lenA = len(A)
        lenB = len(B)
        if lenA > lenB:
            return self.findKthSmallest(B, A, k)
        if lenA == 0:
            return B[k - 1]
        if k == 1:
            return min(A[0], B[0])
        pa = min(k/2, lenA)
        pb = k - pa
        if A[pa - 1] <= B[pb - 1]:
            return self.findKthSmallest(A[pa:], B, pb)
        else:
            return self.findKthSmallest(A, B[pb:], pa)
    def findMedianSortedArrays(self, A, B):
        lenA = len(A); lenB = len(B)
        if (lenA + lenB) % 2 == 1:
            return self.findKthSmallest(A, B, (lenA + lenB)/2 + 1)
        else:
            return (self.findKthSmallest(A, B, (lenA + lenB)/2) + self.findKthSmallest(A, B, (lenA + lenB)/2 + 1)) * 0.5


class Solution_secondRound:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, A, B):
        la, lb = len(A), len(B)
        mid = (la+lb)//2
        if (la+lb)%2:
            isEven = False
        else:
            isEven = True
        merged = []
        if la == 0:
            merged = B[:]
        elif lb == 0:
            merged = A[:]
        else:
            ia, ib =0 ,0
            while ia < la and ib<lb:
                if A[ia]<B[ib]:
                    merged.append(A[ia])
                    ia += 1
                else:
                    merged.append(B[ib])
                    ib += 1
            if ia < la:
                merged += A[ia:]
            if ib<lb:
                merged += B[ib:]
        if isEven:
             return (merged[mid]+merged[mid-1]+0.0)/2
        else:
            return merged[mid]

















