'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

	For example, given array S = {-1 2 1 -4}, and target = 1.

	The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
def threeSumClosest(num, target):
	num.sort()
	n = len(num)
	closet = num[0] + num[1] + num[2]
	for i in range(n-1):
		start, end = i+1, n-1
		while start < end:
			total = num[i] + num[start] + num[end]
			if abs(total-target) < abs(closet-target):
				closet = total
			if total < target:
				start += 1
			elif total > target:
				end -= 1
			else:
				closet = total
				break
	return closet

a = threeSumClosest([1,1,1,0],-100)
print a