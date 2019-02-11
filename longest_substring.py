# 3. Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        letters = {}
        longest_len = 0
        i = 0;
        while i < len(s):
            j = i
            while j < len(s):
                if (letters.get(s[j]) == None):
                    letters[s[j]] = 1
                else:
                    letters = {}
                    break

                if len(letters) > longest_len:
                    longest_len = len(letters)
                j += 1
            i += 1
        return longest_len