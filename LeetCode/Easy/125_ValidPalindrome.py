"""
Problem Link : https://leetcode.com/problems/valid-palindrome/
Platform     : LeetCode
Difficulty   : Easy
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []
        for c in s:
            if c.isalnum():
                result.append(c.lower())
        s = ''.join(result)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left +=1
            right -=1
        return True
