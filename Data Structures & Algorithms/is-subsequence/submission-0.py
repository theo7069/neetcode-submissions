class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0
        count = 0

        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1
                r += 1
                count += 1
                continue
            r += 1
        if count == len(s):
            return True
        return False
        
        