class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stacks = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                b = stacks.pop()
                a = stacks.pop()
                if token == "+":
                    stacks.append(a + b)
                elif token == "-":  
                    stacks.append(a - b)
                elif token == "*":
                    stacks.append(a * b)
                else:
                    stacks.append(int(a / b))        
            else:
                stacks.append(int(token))
        return stacks[0]
