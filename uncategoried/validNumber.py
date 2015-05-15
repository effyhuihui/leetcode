__author__ = 'effy'
'''
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up
front before implementing one.
'''

class Solution:
    def isNumber(self, number):
        def onlyDigit(num):
            if num == '':
                return False
            for s in num:
                if s not in '0123456789':
                    return False
            return True

        num = number.strip()
        if len(num) == 0:
            return False
        # sign
        if num[0] == '+' or num[0] == '-':
            num = num[1:]
        # exponential
        num = num.lower()
        fields = num.split('e')
        first = fields[0]

        if len(fields) > 2:
            return False

        if len(fields) == 2:
            second = fields[1]
            if len(second) == 0:
                return False
            if second[0] == '+' or second[0] == '-':
                second = second[1:]
            if not onlyDigit(second):
                return False

        fields = first.split('.')
        first = fields[0]

        if len(fields) > 2:
            return False

        if len(fields) == 2:
            second = fields[1]
            if second == '':
                return onlyDigit(first)
            if first == '':
                return onlyDigit(second)
            if not onlyDigit(second):
                return False

        if not onlyDigit(first):
                return False

        return True