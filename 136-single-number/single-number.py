class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        found = {}
        
        for num in nums:
            if num not in found:
                found[num] = 1
            else:
                found[num] += 1
        for key, value in found.items():
            if value == 1:
                return key
                