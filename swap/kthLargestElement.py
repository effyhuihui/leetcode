__author__ = 'effy'
## no duplicates
def noDup(nums ,k):
    l = len(nums)
    if l < k:
        return None
    pivot =  nums[l/2]
    next_smaller, next_bigger = 0, l-1
    i = 0
    while i <= next_bigger:
        if nums[i] == pivot:
            i += 1
        elif nums[i] < pivot:
            nums[next_smaller], nums[i] = nums[i], nums[next_smaller]
            i += 1
            next_smaller += 1
        else:
            nums[next_bigger], nums[i] = nums[i],  nums[next_bigger]
            next_bigger -= 1
    if next_smaller == k-1:
        return pivot
    elif next_smaller >=k:
        return noDup(nums[:next_smaller], k)
    else:
        return noDup(nums[next_bigger+1:], k-next_smaller-1)

def dup(nums, k):
    l = len(nums)
    if l < k:
        return None
    pivot = nums[l/2]
    next_small, next_bigger, p_count = 0, l-1,0
    i = 0
    while i<next_bigger:
        if nums[i] == pivot:
            i += 1
            p_count += 1
        elif nums[i] < pivot:
            nums[next_small], nums[i] = nums[i], nums[next_small]
            i += 1
            next_small += 1
        else:
            nums[next_bigger] , nums[i] = nums[i], nums[next_bigger]
            next_bigger -= 1
    if next_small <= k-1 and next_small+p_count<=k:
        return pivot
    elif next_small >=k:
        return noDup(nums[:next_small], k)
    else:
        return noDup(nums[next_bigger+1:], k-next_small-p_count)

print noDup([9,8,7,6,5,4,3,2,1],3)
