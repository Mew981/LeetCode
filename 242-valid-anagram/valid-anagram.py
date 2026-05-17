class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        found = False

        if len(s) != len(t):
            return False

        for letter in s:
            if letter in t:
                found = True
                t = t.replace(letter,"", 1)
        if len(t) > 0:
            found = False
        return found
            
            
            