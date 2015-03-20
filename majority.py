# -*- coding: utf-8 -*-
'''
Given an array of size n, find the majority element. The majority element is the 
element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist 
in the array.
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
num = [1,1,1,1,1,1,2,2,0]
a = majorityElement(num)
print a



















