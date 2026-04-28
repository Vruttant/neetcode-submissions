class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = [] 
        for op in operations:
            if op == "+":
                last, last_second = stack[-1], stack[-2]
                stack.append(int(last) + int(last_second))
            elif op == "C":
                stack.pop()
            elif op == "D":
                last_double = stack[-1] * 2
                stack.append(last_double)
            else:
                stack.append(int(op))
        
        print(stack)
        return sum(stack)

            