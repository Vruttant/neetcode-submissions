class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 

        if len(s) < 2:
            return False

        for b in s:
            if b in ("(", "[", "{"):
                stack.append(b)
            elif b == ")" and len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            elif b == "]" and len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            elif b == "}" and len(stack) > 0 and stack[-1] == "{":
                stack.pop()
            else:
                return False 

        if len(stack) > 0:
            return False

        return True 