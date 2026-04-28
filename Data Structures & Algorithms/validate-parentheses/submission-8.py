class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 

        for b in s:
            
            if b in ("(", "[", "{"):
                stack.append(b)
                continue 

            if len(stack) < 1:
                return False 

            last = stack[-1]

            if b == ")" and last == "(":
                stack.pop() 
            elif b == "]" and last == "[":
                stack.pop() 
            elif b == "}" and last == "{":
                stack.pop()
            else:
                return False
        
        return len(stack) == 0