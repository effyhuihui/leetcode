# -*- coding: utf-8 -*-
'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, 
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) 
are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

Catch: 
only one pair is valid

Thought:
Way 1. use a hash, the key will be the value of the array element, the value will be the 
	   index of the array element O(N)  -- Inverted Index
Way 2. Sort first N*O(logN), and then:
		2.1 either do a binary search, 
		2,2 or do a 'look back and forth', 'back and forth' means 两头看：）， 
	但是Sort有一个问题，因为题中要求的是return原array的index，所以在sort的时候需要maintain原来的index

P.S MergeSort() 参见mergesort.py, binarysearch 参见binarysearch.py
'''
def twoSum1(num,target):
	d = {}
	n = len(num)
	# store the look up key in d, which is the value of [num], and the value of d is the index 
	# possibility is there are two same numbers and they add up to target, so need a list to 
	# to keep index, and also, if there is one number that is half of the target, then look up will
	# succeed, but it should not return 
	for i in range(n):
		v = num[i]
		## d[v] = d.get(v,[]).append(i) will not work
		d[v] = d.get(v, []) + [i]
	for i in range(n):
		cur = num[i]
		res = target-cur
		## look up in dict is O(1)
		if res == cur:
			if len(d[cur]) == 2:
				return d[v][0]+1, d[res][0]+1
			else:
				continue
		else:
			if res in d.keys():
				return i+1, d[res][0]+1
	return False

### WAY TWO
def twoSum2_2(num, target):
	n = len(num)
	indices = [i for i in range(n)]
	## sort indices array according to num[x]
	indices.sort(key=lambda x: num[x])
	start, end = 0, n-1
	## start from the smallest and biggest element from [num] 
	## the index of the smallest element is the first ele in [indices]
	## the index of the biggest element is the last ele in [indices]
	while start != end:
		i, j = indices[start], indices[end]
		res = num[i] + num[j]
		if res == target:
			return min(i+1, j+1), max(i+1, j+1)
		elif res > target:
			end -= 1
		else:
			start += 1
	return False

def twoSum2_1(num, target):
	new = sorted(num)
	n = len(new)
	found = False
	for i in range(n):
		if found:
			break
		res = target-new[i]
		## binary search
		# set starting index
		start ,end = i, n-1	
		while start < end:
			k = (end-start)//2 + start
			cur = new[k]
			if cur == res:
				found = True
				break
			elif cur > res:
				end = k - 1
			else:
				start = k + 1
	if found:
		return i-1,k
	else:
		return False

a,b = twoSum1([3,2,4], 6)
print a,b





class Solution_secondround:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        index = [i for i in range(len(num))]
        index.sort(key=lambda x: num[x])
        start, end = 0, len(num)-1
        while start < end:
            if num[index[start]] + num[index[end]] == target:
                return (min(index[start]+1,index[end]+1), max(index[start]+1,index[end]+1))
            if num[index[start]] + num[index[end]] < target:
                start += 1
            else:
                end -= 1
        return False
























