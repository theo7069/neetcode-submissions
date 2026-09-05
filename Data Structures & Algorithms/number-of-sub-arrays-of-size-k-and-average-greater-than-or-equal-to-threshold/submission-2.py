class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        sum = 0
        average = 0
        for i in range(k):
            sum += arr[i]
        average = sum / k
        if average >= threshold:
            count += 1
        l = 0
        new_sum = 0
        for i in range(k, len(arr)):
            new_sum = average * k
            new_sum += arr[i]
            new_sum -= arr[l]
            average = new_sum / k
            if average >= threshold:
                count+= 1
            l += 1
        return count



        