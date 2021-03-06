# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
You are given a string, S, and a list of words, L, that are all of the same length.
Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once
and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

Note: there could be same word in L:
S: "lingmindraboofooowingdingbarrwingmonkeypoundcake"
L: ["fooo","barr","wing","ding","wing"]
thoughts:
same as "longest substring without any repeat characters", two pointers and a "hash map"

解题思路：使用一个字典统计一下L中每个单词的数量。由于每个单词的长度一样，以题中给的例子而言，可以3个字母3个字母的检查，
如果不在字典中，则break出循环。有一个技巧是建立一个临时字典curr，用来统计S中那些在L中的单词的数量，必须和L中单词的数量相等，
否则同样break。
'''
'''
This is the fastest 98ms
'''
class Solution_effy:
    def findSubstring(self, S, L):
        n, l = len(L),len(L[0])
        words = {}
        for i in L:
            words[i] = words.get(i,0)+1
        res = []
        ## l is the offset(就和相位一样，如果每个word长度为3，可以从0，1，2开始，分别三个三个看)
        for i in range(l):
            curr = {}
            count = 0
            ## 每一个相位对应的curr map是可以重复利用的
            for j in range(i,len(S)-n*l+1,l):
                cur = S[j:j+l]
                ## 尝试着找一个完整的substring
                while cur in words and count < n:
                    if curr.get(cur,0) < words[cur]:
                        curr[cur] = curr.get(cur,0)+1
                        count += 1
                    else:
                        break
                    cur = S[j+count*l:j+count*l+l]
                if count == n:
                    res.append(j)
                ## since next cur will start from the next word, remove the previous start word
                if S[j:j+l] in curr:
                    count -=1
                    curr[S[j:j+l]] -= 1
                ## remove the next cur from curr dict:
                ## there is something worth noticing here:
                ## if S[j+l: j+2*l] in words, then it must been proccessed in the while loop
                ## and get recorded in the curr dict already, need to be removed, if it is not
                ## then the following if statement will be skipped anyway.
                if S[j+l:j+l*2] in curr:
                    count -= 1
                    curr[S[j+l:j+l*2]] -= 1
        return res

class Solution_seoncdround:
    def findSubstring(self, S, L):
        L.sort()
        l_word = len(L[0])
        num_of_words= len(L)
        word_map = {i:True for i in L}
        inverted_map = {}
        res = []
        ## all starting indices that is valid in L
        for i in range(len(S)):
            cur = S[i:i+l_word]
            if cur in word_map:
                inverted_map[i] = cur
        for i in range(len(S)-num_of_words*l_word+1):
            all_words = []
            for j in range(num_of_words):
                if i+j*l_word in inverted_map:
                    all_words.append(inverted_map[i+j*l_word])
                else:
                    break
            if len(all_words) == num_of_words and sorted(all_words) ==L:
                res.append(i)
        return res


x = Solution_effy()
print x.findSubstring("aaaaaaaa", ["aa","aa","aa"])




