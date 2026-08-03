class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numbers = "".join(map(str, digits))
        nums = int(numbers)
        nums = nums + 1
        ans = str(nums)
        list2 = []
        for i in range(len(ans)):
            list2.append(int(ans[i]))
        return list2

        