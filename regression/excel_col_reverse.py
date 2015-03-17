'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''
def re(n, num):
	if num >= 26:
		n = re(n+1, num//26)
	return n

print re(0,17576)





def convertToTitle(num):
	res = ''
	bu = []
	def currentLargest(num):
		n = 0
		div = 26**n
		residual = num
		while residual > div:
			residual = num%div
			n += 1
		return n, num//div, residual

	while num >= 26:
		n, residual = currentLargest(num)
		num = residual	
		bu.append(n)
	return bu































	

	