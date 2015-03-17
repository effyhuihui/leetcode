__author__ = 'effy'
'''
Given a range of integers(inclusive), return how many square numbers are there in the range.
e.g.:
[4,17] returns 3. Since 4,9,16 are square numbers
[3,17] returns 3. Same reason

'''
def solution(A,B):
    def sqrt(x):
        if x == 0:
            return 0
        if x == 1:
            return 1
        start = 1
        end = x/2
        while start <= end:
            mid = (start + end)/2
            if mid*mid <= x and (mid+1)*(mid+1) > x:
                return mid
            elif mid*mid > x:
                end = mid - 1
            else:
                start = mid + 1
            mid = (start + end)/2
        return mid
    if B < 0:
        return 0
    else:
        end = sqrt(B)
        if A <=0:
            start = 0
        else:
            start = sqrt(A)
            if start*start < A:
                start +=1
    return end-start+1
print solution(4,17)