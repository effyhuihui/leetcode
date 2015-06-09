__author__ = 'effy'
'''
String s1 = "waeginsapnaabangpisebbasepgnccccapisdnfngaabndlrjngeuiogbbegbuoecccc";
String s2 = "a+b+c-";
'+' means there are two chars of the previous char, - means there are four previous chars ('a+b+c-' = 'aabbcccc').
assuming there is no error in representing s2, find the count of unique subsequence in s1
'''
count = 0
def distinctSubsequence_dfs(s1,s2):
    l1, l2 = len(s1),len(s2)
    def dfs(s1_index,s2_index):
        global count
        if s2_index == l2:
            count += 1
        else:
            next_match_char = s2[s2_index]
            if s2[s2_index+1] == '+':
                offset = 2
            else:
                ## '='
                offset = 4
            for i in range(s1_index+offset, l1+1):
                if s1[i-offset:i] == next_match_char*offset:
                    dfs(i,s2_index+2)
    dfs(0,0)
    return count

#print distinctSubsequence_dfs('aaebbdccccaabbcccc', 'a+b+c-')



def distinctSubsequence_dp(s1,s2):
    l1, l2 = len(s1), len(s2)
    dp = [ [0 for i in range(l1+1)] for j in range(l2+1)]
    for i in range(l1+1):
        dp[0][i] = 1
    for i in range(2,l2+1,2):
        next_match_char = s2[i-2]
        if s2[i-1]=='+':
            char_count = 2
        else:
            char_count = 4
        for j in range(char_count,l1+1):
            if s1[j-char_count:j] == char_count*next_match_char:
                dp[i][j]=dp[i-2][j-char_count]+dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[-1][-1]

print distinctSubsequence_dp('aaebbdccccaabbcccc', 'a+b+c-')

