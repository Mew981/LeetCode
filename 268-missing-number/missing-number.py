class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        compare = []
        nums.sort()
        for i in range(n + 1):
            compare.append(i)
        
        for num in compare:
            if num not in nums:
                return num

