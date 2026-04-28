class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for tkn in tokens:
            if tkn == "+":
                operands.append(operands.pop() + operands.pop())
            elif tkn == "-":
                b = operands.pop()
                a = operands.pop()
                operands.append(a - b)
            elif tkn == "*":
                operands.append(operands.pop() * operands.pop())
            elif tkn == "/":
                b = operands.pop()
                a = operands.pop()
                operands.append(int(a / b))
            else:
                operands.append(int(tkn))
        return operands[0]