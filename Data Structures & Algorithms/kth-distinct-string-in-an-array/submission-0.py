class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res = []

        for i in range(len(arr)):
            count = 0

            for j in range(len(arr)):
                if i != j and arr[i] == arr[j]:
                    count += 1

            if count == 0:
                res.append(arr[i])

        if len(res) >= k:
            return res[k - 1]

        return ""
        