class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        front_brackets = {"(", "{", "["}
        brackets_map = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in front_brackets:
                stack.append(c)
            else:
                if not stack or stack[-1] != brackets_map[c]:
                    return False
                else:
                    stack.pop()
        if stack: return False              
        return True
