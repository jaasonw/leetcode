# 7. Reverse Integer
# Given a 32-bit signed integer, reverse digits of an integer.
class Solution(object):
    def reverse(self, x):
        sum = 0
        _x = abs(x) if x < 0 else x
        while _x != 0:
            sum *= 10
            sum += _x % 10
            _x = int(_x / 10)
        if abs(sum) > 2147483647:
            return 0
        if x >= 0:
            return sum
        if x < 0:
            return -sum
