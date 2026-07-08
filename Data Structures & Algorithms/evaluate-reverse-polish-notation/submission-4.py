class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token in operators:
                if token == '+':
                    result = stack[len(stack)-2] + stack[len(stack)-1]
                    stack.pop()
                    stack[len(stack) - 1] = result
                elif token == '-':
                    result = stack[len(stack)-2] - stack[len(stack)-1]
                    stack.pop()
                    stack[len(stack) - 1] = result
                elif token == '*':
                    result = stack[len(stack)-2] * stack[len(stack)-1]
                    stack.pop()
                    stack[len(stack) - 1] = result
                else:
                    result = int(stack[len(stack)-2] / stack[len(stack)-1])
                    stack.pop()
                    stack[len(stack) - 1] = result

            else:
                stack.append(int(token))
            print(stack)
        return stack[0]
