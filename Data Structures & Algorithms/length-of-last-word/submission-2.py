class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        r = len(s) - 1

        while not s[r].isalpha():
            r -= 1
        l = r
        if l == 0:
            return 1 

        while s[l] and s[l].isalpha():
            l -= 1
        
        return r - l
            
        
