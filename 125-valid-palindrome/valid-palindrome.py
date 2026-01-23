class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        list = []
        
        for i in s:
            if i.isalnum():
                list.append(i)
            continue
            

        return list == list[::-1]