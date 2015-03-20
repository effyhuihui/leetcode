'''
compare() takes two string in, returns True if they need to swap
False if not
'''
def compare(a, b):
    i, j = 0, 0
    p, q = len(a), len(b)
    while i < p and j < q:
        if a[i] > b[i]:
            return False
        elif a[i] < b[i]:
            return True
        else:
            i += 1
            j += 1
    if i < p:
        if a[i] > b[0]:
            return False
        else:
            return True
    if j < q:
        if b[j] > a[0]:
            return True
        else:
            return False



num = [0,0,0]
n = len(num)
print sum(num)
for i in range(1,n):
    s, m = str(num[i-1]), str(num[i])
    j, k = i-1, i
    while compare(s,m) and j >= 0:
        num[j] = m
        num[k] = s
        j -= 1
        k -= 1
        s = str(num[j])
        m = str(num[k])
        print num
c = [str(i) for i in num]
print ''.join(c)
