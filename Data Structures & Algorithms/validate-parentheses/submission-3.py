class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {")":"(", "]":"[", "}":"{"}
        for bracket in s:
            if bracket in parentheses:
                if stack and stack[-1] == parentheses[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        if len(stack) != 0:
            return False
        return True