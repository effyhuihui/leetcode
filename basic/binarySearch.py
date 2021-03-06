'''
very standard binary search code
Catch:
1. inside while loop, end and start can not be "fixed", this will cause infinite loop, for cases like
   [0,2,7,8] to search 5, because start and end will approach to be neighbors, meaning in the very 
   last step, end and start will only be 1 index away, so k = (end-start)//2+start = start, in the case
   for cur < res, start = k = start, this will cause a infinite loop
   (TO CHECK WHETHER WILL THERE BE INFINITE LOOP, CHECK IF THERE ANY STEP THAT COULD CAUSE A FIX POINT)
2. k = (end-start)//2 + start is equivalent to (end+start)//2, however, this is safer, because when start
   and end are big, adding them together will cause overflow.
'''
def binarySearch(num, res):
    '''
    Binary Search has no constrains. It allows the array of numbers to have
    duplicates.
    '''
    n = len(num)
    start ,end = 0, n-1
    while start <= end:
        mid = (end-start)//2 + start
        cur = num[mid]
        if cur == res:
            return True
        elif cur > res:
            end = mid - 1
        else:
            start = mid + 1
    return False

r = binarySearch([0,0,0,0,2,7,8],2)
print r