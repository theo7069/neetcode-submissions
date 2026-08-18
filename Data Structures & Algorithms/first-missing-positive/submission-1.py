class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numbers = set(nums)
        res = 1

        while res in numbers:
            res += 1

        return res
        