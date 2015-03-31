__author__ = 'effy'
'''
Given a string S and a string T, find the minimum window in S
which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one
unique minimum window in S.
'''
class Solution:
    # @return a string
    def minWindow(self, S, T):
        start = 0
        min_len = len(S)
        min_win = S
        char_count = {}
        all_appear = False
        for i in T:
            char_count[i] = char_count.get(i,0)+1
        for index in range(len(S)):
            char = S[index]
            if char in char_count:
                char_count[char] -= 1
                if not all_appear:
                    all_appear = all([i <= 0 for i in char_count.values()])
                if all_appear:
                    temp = S[start]
                    while temp not in char_count or char_count[temp] < 0:
                        start += 1
                        if temp in char_count:
                            char_count[temp] += 1
                        temp = S[start]
                    l = index-start+1
                    if l < min_len:
                        min_len = l
                        min_win = S[start:index+1]
        if not all_appear:
            return ""
        return min_win


class Solution1:
    # @return a string
    def minWindow(self, S, T):
        last_start,next_start = 0,0
        min_win = S
        ## how to check all characters in T appear?
        ## check all values in char_map is less/equal to 0
        all_appear = False
        char_map = {}
        for i in T:
            char_map[i] = char_map.get(i,0)+1
        for i in range(len(S)-len(T)+1):
            cur = S[i]
            if cur not in char_map:
                last_start = next_start
                count = min(len(T), count+1)
            else:
                char_map[cur] -= 1
                if last_start == next_start:
                    next_start = i
                all_appear = all([i <= 0 for i in char_map.values()])
                if all_appear:
                    cur_win = S[last_start:i]
                    if len(cur_win) < len(min_win): min_win = cur_win
                    char_map[S[last_start]] += 1
                    last_start = next_start
        if not all_appear:
            return ""
        return min_win