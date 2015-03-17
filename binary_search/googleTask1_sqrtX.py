__author__ = 'effy'
def solution(A,B):
    def sqrt(x):
        if x == 1:
            return 1
        start = 1
        end = x/2
        mid = (start+end)/2
        while start < end:
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
    return end-start+1
print solution(4,17)