__author__ = 'effy'
class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, a, b, c, d, e, f, g, h):
        width = self._overlap_len(a, c, e, g)
        height = self._overlap_len(b, d, f, h)
        return (c - a) * (d - b) + (g - e) * (h - f) - width * height

    def _overlap_len(self, a, b, c, d):
        if a > c:
            a, b, c, d = c, d, a, b
        if c < b < d:
            return b - c
        if d <= b:
            return d - c
        return 0