# -*- coding: utf-8 -*-
'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
	For example, given array S = {-1 0 1 2 -1 -4},

	A solution set is:
	(-1, 0, 1)
	(-1, -1, 2)

Catch:
只有一个confusing的地方，就是去重
'''
def threeSum(num):
	#O(Nlg(N))
	num.sort()
	res = []
	n = len(num)
	# O(N**2) 两头看
	for i in range(n-1):
		cur = num[i]
		## if cur is the same as previous cur, continue
		if i > 0 and cur == num[i-1]:
			continue
		target = -cur
		j, k = i+1, n-1
		while j < k:
			tmp = num[j] + num[k]
			if tmp > target:
				k -= 1
			elif tmp < target:
				j += 1

			else:
				res.append([num[i], num[j], num[k]])
				j += 1
				## if found a match, move j to the index where num[j] is different with the previous num[j] to avoid duplicates
				while j < n and num[j] == num[j-1]:
					j += 1

	return res


class Solution_secondround:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        res = []
        l = len(num)
        for i in range(l):
            ## check for duplicates!!!
            if i>=1 and num[i] == num[i-1]:
                continue
            else:
                target = -num[i]
                start, end = i+1,l-1
                while start<end:
                    if num[start]+num[end] == target:
                        res.append([num[i],num[start],num[end]])
                        start += 1
                        while num[start] == num[start-1] and start < end:
                            start += 1
                    elif num[start] + num[end] > target:
                        end -= 1
                    else:
                        start +=1
        return res

x = threeSum([-1, 0, 1, 2, -1, -4])
print x

def threeSum_hash(num):
	num.sort()
	res = []
	n = len(num)
	record = {}
	for i in num:
		record[i] = record.get(i, 0) + 1
	for i in range(n-1):
		## if the current value is the same as previous value, it will cause duplicates, pass and continue
		if i > 0 and num[i] == num[i-1]:
			continue
		for j in range(i+1,n):
			target = -(num[i]+num[j])
			if (target == num[i] and target == num[j] and record.get(target,0) == 3) or (target == num[i] and record.get(target,0)==2) or (target == num[j] and record.get(target,0)==2) or (target in record.keys()):
				res.append([num[i],num[j],target])
				prev = num[j]
				while j<n and prev == num[j]:
					j+=1
	return res


