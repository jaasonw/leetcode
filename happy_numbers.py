# 202. Happy Number
# Write an algorithm to determine if a number n is "happy".
# A happy number is a number defined by the following process: Starting with 
# any positive integer, replace the number by the sum of the squares of its 
# digits, and repeat the process until the number equals 1 (where it will stay), 
# or it loops endlessly in a cycle which does not include 1. Those numbers for 
# which this process ends in 1 are happy numbers.
# Return True if n is a happy number, and False if not.

class Solution:
    def isHappy(self, n: int) -> bool:
        input_as_string = str(n)
        numbers = {}
        while True:
            squared_sum = 0
            for num in input_as_string:
                squared_sum += int(num) ** 2
            if squared_sum == 1:
                return True
            if input_as_string in numbers:
                return False
            else:
                numbers[input_as_string] = squared_sum
            input_as_string = str(squared_sum)
