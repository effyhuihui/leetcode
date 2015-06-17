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


class Solution_secondround:
    # @return a string
    def minWindow(self, S, T):
        target_l = len(T)
        target_dict = {}
        for i in T:
            target_dict[i] = target_dict.get(i,0)+1
        start =0
        l = len(S)
        min_window = S
        cur_word_map = {i:0 for i in T}
        total_valid_char = 0
        hasWindows = False
        for i in range(l):
            if S[i] in target_dict:
                cur_word_map[S[i]] += 1
                if cur_word_map[S[i]] <= target_dict[S[i]]:
                    total_valid_char += 1
            while total_valid_char == target_l:
                hasWindows = True
                ## assign min window
                if i-start<len(min_window):
                    min_window = S[start:i+1]
                ## update cur_word_map
                if S[start] in cur_word_map:
                    cur_word_map[S[start]] -=1
                    if cur_word_map[S[start]] < target_dict[S[start]]:
                        total_valid_char -= 1
                start += 1
        if hasWindows:
            return min_window
        else:
            return ''