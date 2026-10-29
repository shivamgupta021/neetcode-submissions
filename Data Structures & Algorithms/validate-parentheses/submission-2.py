class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        brackets = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        stack = []
        
        for bracket in s:
            if stack:
                expected = brackets.get(stack[-1], None)
                if bracket == expected:
                    stack.pop()
                    continue
            stack.append(bracket)

        if len(stack) == 0:
            return True

        return False
