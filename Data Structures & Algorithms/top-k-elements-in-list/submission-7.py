class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        number_list = []
        for key, value in count.items():
            number_list.append([key,value])
        number_list.sort(key= lambda x:x[1], reverse = True)
        res = []
        for i in range(k):
            res.append(number_list[i][0])
        return res
