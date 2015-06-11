__author__ = 'effy'
'''
Input: str="abcdeefuiuiwiwwaaaa" n=3 output: "iwiwwaaaa" (longest substr with 3 diff chars)
'''
'''

There is an O(n). Let S be the string. Just go through the array with two pointers
 i and j and keep track of number K of different letters between S[i] and S[j].
 Increment j whenever this number is smaller or equal n and increment i whenever K
 is greater than n. Also remember the longest substring for which K was equal to n.

In the implementation you also need a hash table to keep track of the last
occurrence of the letter.


'''
'''
typically in two pointer problems, while loop has two types of conditions, one for
start pointer, one for end pointer.
ONE WHILE LOOP should be sufficient for both moving end forward and moving start forward
Just list out different types of conditions and then process them,
'''
def longest(S,n):
    i = j = K = 0
    res = (0,0)
    last_seen = {}

    while i < len(S) and j < len(S):
        # if current substring is better than others than save
        if K == n and j - i > res[1] - res[0]:
            res = (i,j)

        # if we can go further with the right end than do it
        if K <= n :
            if not last_seen.has_key(S[j]):
                K = K + 1
            last_seen[S[j]] = j
            j = j + 1
        # if we must go further with the left end than do it(k>n)
        else:
            if last_seen[S[i]] == i:
                del last_seen[S[i]]
                K = K - 1
            i = i + 1
    return S[res[0]:res[1]]
#print longestUnique('aaabbccddddaa',4)

def longestUnique(s, k):
    ## create an associate array
    compress_s, count_array = '',[]
    prev,count = s[0],1
    for i in range(1,len(s)):
        if s[i] != prev:
            compress_s += prev
            count_array.append(count)
            prev = s[i]
            count = 1
        else:
            count += 1

    last_seen = {}
    start,end,char_count = 0, 0, 0
    substring = (0,0)
    while start<end and end<len(compress_s):
        if char_count == k and end-start > substring[1]-substring[0]:
            substring = (start,end)
        if char_count <= k:
            if last_seen[compress_s[end]] < start:
                char_count += 1
            last_seen[compress_s[end]] = end
            end += 1
        else:
            if last_seen[compress_s[start]] == start:
                k -= 1
            start += 1
    return substring
