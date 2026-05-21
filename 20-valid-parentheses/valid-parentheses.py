class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        a = []

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                a.append(s[i])
            else:
                if not a:
                    return False
                t = a.pop() #t=opening bracket and a should be empty
                if s[i] == ")" and t != "(":
                    return False
                if s[i] == "]" and t != "[":
                    return False
                if s[i] == "}" and t != "{":
                    return False
        return len(a) == 0
        



        