__author__ = 'effy'
'''
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG".
When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
'''


'''
Both solutions pass.
First is mine
'''
class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        l = len(s)
        occurs = {}
        res = []
        for i in range(l-9):
            cur = s [i:i+10]
            occured_and_appended = occurs.get(cur,0)
            if occured_and_appended == 1:
                res.append(cur)
                occurs[cur] += 1
            elif occured_and_appended == 0:
                occurs[cur] = 1
            else:
                occurs[cur] += 1
        return res

class Solution2:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        dic ,ans, n=set(),set(),len(s)
        for i in range(n-9):
            cur = s[i:i+10]
            if cur in dic:
                ans.add(cur)
            else: dic.add(cur)
        return list(ans)



class Solution_secondround:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        appeared = {}
        res = []
        l = len(s)
        for i in range(l-9):
            cur_sequence = s[i:i+10]
            if cur_sequence in appeared:
                if appeared[cur_sequence] ==1:
                    res.append(cur_sequence)
                appeared[cur_sequence]+=1
            else:
                appeared[cur_sequence] = 1
        return res
x =  Solution2()
print x.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")