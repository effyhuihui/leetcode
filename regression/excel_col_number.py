def titleToNumber(s):
	'''
	Given a column title as appear in an Excel sheet, return its 
	corresponding column number.

	For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

    Catch:
    Nothing much

    Thoughts:
    It is a 26 decimal operation
	'''
	res = 0
	l = len(s)
	for i in range(l):
		res += (26**i)*(ord(s[l-i-1])-64)
	return res


print titleToNumber("BA")
