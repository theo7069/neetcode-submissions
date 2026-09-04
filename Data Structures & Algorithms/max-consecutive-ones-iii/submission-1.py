class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = {}
        res = 0
        l = 0
        for r in range(len(nums)):
            count[nums[r]] = 1 + count.get(nums[r], 0)
            if 0 in count:
                if count[0] > k:
                    count[nums[l]] -= 1
                    l += 1
            res = max(res, r - l + 1)
        return res

        