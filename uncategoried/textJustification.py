__author__ = 'effy'
'''
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully
(left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not
divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.
'''

class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        cur_start, cur_end =0, 0
        l = len(words)
        res = []
        while cur_start < l:
            sameLineLength = 0
            stringLength = 0
            while sameLineLength < maxWidth and cur_end<l:
                cur_len = len(words[cur_end])
                if cur_end == cur_start:
                    ## each word will not exceed maxWidth
                    sameLineLength += cur_len
                else:
                    if sameLineLength + cur_len + 1 <= maxWidth:
                        sameLineLength += cur_len + 1
                    else:
                        break
                stringLength += cur_len
                cur_end += 1

            wordNum = cur_end-cur_start
            ## corner case for only one word, left justification
            if wordNum == 1:
                res.append(words[cur_start]+' '*(maxWidth-len(words[cur_start])))
            else:
                evenSpace = (maxWidth-stringLength)//(wordNum-1)
                extraSpace = (maxWidth-stringLength)%(wordNum)
                line = ''
                count = 0
                for i in range(cur_start,cur_end):
                    if count < extraSpace:
                        line += words[i] + ' '*(evenSpace+1)
                    elif count >= extraSpace and count < wordNum-1:
                        line += words[i] +' '*evenSpace
                    else:
                        line += words[i]
                    count += 1
                res.append(line)
            cur_start = cur_end
        return res
x = Solution()
print x.fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16)


