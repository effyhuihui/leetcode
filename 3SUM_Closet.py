'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
def threeSumClosest(num, target):
	num.sort()
	cur_diff = float("inf")
	cur_total = 0
	n = len(num)
	for i in range(n-1):
		j, k = i+1, n-1
		while j < k:
			total = num[i] + num[j] + num[k]
			diff = abs(total-target)
			if diff == 0:
				return total
			if diff < cur_diff:
				cur_total = total
				cur_diff = diff
			if total > target:
				k -= 1
			else:
				j += 1
	return cur_total

a = threeSumClosest([1,1,1,0],-100)
print a
