__author__ = 'effy'
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if x == 0:
            return 0
        elif x < 0:
            sign = '-'
        else:
            sign = ''
        l = []
        absx = abs(x)
        while absx:
            l.append(str(absx%10))
            absx = absx/10
        return int(sign+''.join(l))

class Solution:
    # @return an integer
    def reverse(self, x):
        l = []
        y = abs(x)
        while y:
            l.insert(0,y%10)
            y = y/10
        r = ''
        while len(l):
            r += str(l.pop())
        if x < 0 :
            return int('-'+r)
        elif x == 0:
            return 0
        else:
            return int(r)