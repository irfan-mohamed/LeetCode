class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []
        for element in s:
            if element in pairs:
                stack.append(element)
            else:
                if not stack or pairs[stack[-1]] != element :
                    return False
                else:
                    stack.pop()
        return len(stack) == 0