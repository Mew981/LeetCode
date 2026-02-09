class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        string = []

        for letter in s:
            if letter.isalnum():
                string.append(letter)
        
        return string == string[::-1]