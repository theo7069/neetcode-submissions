class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            a = nums[i]

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = a + nums[l] + nums[r]

                if total < 0:
                    l += 1

                elif total > 0:
                    r -= 1

                else:
                    res.add((a, nums[l], nums[r]))
                    l += 1
                    r -= 1

        return [list(triplet) for triplet in res]
        