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



class Solution_secondround:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        closet_sum = num[0]+num[1]+num[2]
        l = len(num)
        for i in range(l):
            if i>=1 and num[i] == num[i-1]:
                continue
            start, end = i+1, l-1
            while start<end:
                total = num[i]+num[start]+num[end]
                if total == target:
                    return total
                if abs(total-target) < abs(closet_sum-target):
                    closet_sum = total
                if total>target:
                    end -= 1
                else:
                    start +=1
        return closet_sum
a = threeSumClosest([1,1,1,0],-100)
print a

class Solution_3rd:
    # @return an integer
    def threeSumClosest(self, num, target):
        closet_sum = num[0]+num[1]+num[2]
        l = len(num)
        num.sort()
        for i in range(l):
            start,end = i+1, l-1
            while start<end and end< l:
                current_sum = num[i] + num[start] + num[end]
                print current_sum
                if abs(target-closet_sum) > abs(current_sum-target):
                    closet_sum = current_sum
                    print closet_sum
                if current_sum == target:
                    return closet_sum
                elif current_sum > target:
                    end -= 1
                else:
                    start += 1
        return closet_sum

x = Solution_3rd()
print x.threeSumClosest([0,0,0], 1)
