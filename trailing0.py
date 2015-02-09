def trailing_zero(n):
	'''
	computes the number of trailing zeros in n!
	'''
	tenth = n//10
	residual = n%10

	add = 0 
	if residual >= 5:
		add = 1
	number_of_zero = tenth*2 + add
	return number_of_zero

def main():
	a = trailing_zero(20)
	out = 1
	for i in range(20):
		out *= i+1
	print a, out
if __name__ == "__main__":
	main()
