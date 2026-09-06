class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            # left edge
            if m == 0:
                if len(nums) == 1 or nums[m] > nums[m + 1]:
                    return m
                l = m + 1
                continue

            # right edge
            if m == len(nums) - 1:
                if nums[m] > nums[m - 1]:
                    return m
                r = m - 1
                continue

            # middle: check both neighbors
            if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                return m

            # right side is going uphill
            if nums[m + 1] > nums[m]:
                l = m + 1

            # left side is going uphill
            else:
                r = m - 1

        