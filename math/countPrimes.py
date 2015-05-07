__author__ = 'effy'
'''
Description:

Count the number of prime numbers less than a non-negative number, n
'''
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <2:
            return 0
        isPrime = [True for i in range(n)]
        isPrime[0],isPrime[1] = False, False
        x = 2
        while x*x<n:
            if isPrime[x]:
                p = x*x
                while p<n:
                    isPrime[p] = False
                    p += x
            x += 1
        return sum(isPrime)
