class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        sum = 0
        l = 0
        res = 0

        for i in range(len(nums)):
            sum += nums[i]

            if (nums[i] * (i - l + 1)) - sum > k:
                sum -= nums[l]
                l += 1
            res = max(res,  i - l + 1)
        return res








        