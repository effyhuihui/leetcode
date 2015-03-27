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

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        ## in one iteration, store whether one word has appeared or not
        appeared = {}
        for i in L:
            appeared[i] = appeared.get(i,0)+1
        res = []
        l = len(L[0])
        i = 0
        while i < len(S):
            start = i
            cur = S[i:i+l]
            occurance_map = {}
            print "start as", start
            count = len(L)
                ## if cur is a word in L and has not appeared since start index
            while i < len(S) and cur in appeared.keys():
                print cur
                occurance_map[cur] = occurance_map.get(cur,0)+1
                if occurance_map[cur] <= appeared[cur]:
                    count -= 1
                    i += l
                    ## if all words has been seen since start
                    if not count:
                        res.append(start)
                        break
                ## if there is word that appeared more than once without all words been appeared, pass
                else:
                    break
                cur = S[i:i+l]
            print "start ends",start
            if start == i:
                i += 1
            print "i",i


        return res


class Solution2:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        words={}
        wordNum=len(L)
        for i in L:
            if i not in words:
                words[i]=1
            else:
                words[i]+=1
        wordLen=len(L[0])
        res=[]
        for i in range(len(S)+1-wordLen*wordNum):
            curr={}
            count=0
            while count<wordNum:
                word=S[i+count*wordLen:i+count*wordLen+wordLen]
                if word not in words:
                    break
                if word not in curr:
                    curr[word]=1
                else:
                    curr[word]+=1
                if curr[word]>words[word]: break
                count+=1
            if count==wordNum: res.append(i)
        return res


x = Solution()
print x.findSubstring("aaa", ["a","a"])




