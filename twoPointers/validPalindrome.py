__author__ = 'effy'
'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and
ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = s.lower()
        front, back = 0, len(s)-1
        ## never move front and back inside a same loop!!!!!
        while front<back:
            if not s[front].isalnum():
                front += 1
            elif not s[back].isalnum():
                back -= 1
            elif s[front] != s[back]:
                return False
            else:
                front += 1
                back -= 1
        return True


class Solution_secondround:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        def validChar(char):
            if char not in '0123456789' and (ord(char)<97 or ord(char)>122):
                return
            return True
        new = s.lower().strip()
        l = len(new)
        left,right = 0, l-1
        if not s:
            return True
        while left<=right:
            while left<right and not validChar(new[left]):
                left += 1
            while right>left and not validChar(new[right]):
                right -=1
            if new[left] != new[right]:
                return False
            left += 1
            right -= 1
        return True



x = Solution()
print x.isPalindrome("a.")