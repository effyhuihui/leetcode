__author__ = 'effy'
'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
'''


class Solution_secondround:
    def countAndSay(self,n):
        prev = '1'
        if n == 1:
            return '1'
        for i in range(n-1):
            cur = ''
            prev_char = prev[0]
            count = 1
            for j in range(1,len(prev)):
                if prev[j] == prev_char:
                    count += 1
                else:
                    cur = cur+ str(count) + prev_char
                    count =1
                    prev_char =prev[j]
            cur = cur+ str(count) + prev_char
            prev = cur
        return cur