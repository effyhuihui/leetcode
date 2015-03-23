'''
Largest Number
'''
'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

compare() takes two string in, returns True if they need to swap
False if not
'''

class Solution_bad:
    def sort(self, nums):
        res = []
        l = len(nums)
        if l <= 1:
            return nums
        pre = self.sort(nums[:l//2])
        post = self.sort(nums[l//2:])
        c1, c2, e1,e2 = 0, 0, len(pre), len(post)
        while c1 < e1 and c2 < e2:
            if self.compare(pre[c1], post[c2]):
                res.append(post[c2])
                c2 += 1
            else:
                res.append(pre[c1])
                c1 += 1
        if c1 < e1:
            res += pre[c1:]
        if c2 < e2:
            res += post[c2:]
        return res

    def compare(self, a, b):
        '''
        compare a and b
        :return: True if a < b, False if a > b
        '''
        pre = int(''.join([str(a),str(b)]))
        post = int(''.join([str(b),str(a)]))
        if pre-post >= 0:
            return False
        else:
            return True

    def largestNumber(self, num):
        res = self.sort(num)
        if res[0] == 0:
            return "0"
        r = [str(i) for i in res]
        return ''.join(r)


class Solution:
    def largestNumber(self, num):
        '''
        cmp specifies a custom comparison function of two arguments (iterable elements) which should return
        a negative, zero or positive number depending on whether the first argument is considered
        smaller than, equal to, or larger than the second argument: if increasing order, if want to decrease,
        need to reverse
        '''
        res = sorted([str(x) for x in num],cmp=self.compare)
        if res[0] == 0:
            return "0"
        return ''.join(res)

    def compare(self,a,b):
        pre = ''.join([str(a),str(b)])
        post = ''.join([str(b),str(a)])
        if int(pre) >= int(post):
            return -1
        else:
            return 1

a = Solution_bad()
print a.largestNumber([121,12])
