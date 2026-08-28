class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        res = float("inf")
        iterations = (len(blocks) - k) + 1
        for i in range(iterations):
            wcount = 0
            for j in range(i, i + k):
                if blocks[j] == "W":
                    wcount += 1
            res = min(res, wcount)
        return res
            
            


        