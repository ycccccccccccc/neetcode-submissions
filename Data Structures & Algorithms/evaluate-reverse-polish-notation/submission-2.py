class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokens_stack = []
        ops = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in ops:
                tokens_stack.append(int(token))
            else:
                val2, val1 = tokens_stack.pop(), tokens_stack.pop()
                if token == "+":
                    tokens_stack.append(val1 + val2)
                elif token == "-":
                    tokens_stack.append(val1 - val2)
                elif token == "*":
                    tokens_stack.append(val1 * val2)
                else:
                    tokens_stack.append(int(val1 / val2))
        return tokens_stack[0]