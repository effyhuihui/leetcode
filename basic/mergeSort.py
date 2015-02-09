def mergeSort(num):
	res = []
	n = len(num)
	if n <= 1:
		return num
	pre = mergeSort(num[ : n//2])
	post = mergeSort(num[n//2 : ])
	l, k, m,n = 0, 0, len(pre), len(post)
	while l < m and k < n:
		if pre[l] <= post[k]:
			res.append(pre[l])
			l += 1
		else:
			res.append(post[k])
			k += 1
	if l < m:
		res += pre[l:]
	if k < n:
		res += post[k:]
	return res

a = mergeSort([10,3,5])



