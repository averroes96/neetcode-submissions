class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        result = None

        def do_math(first, second, operator):
            match(operator):
                case "+": return int(first + second)
                case "-": return int(second - first)
                case "*": return int(first * second)
                case "/": return int(second / first)

        for token in tokens:
            try:
                stack.append(int(token))
            except:
                first = stack.pop()
                second = stack.pop()
                result = do_math(first, second, token)
                stack.append(result)
        
        return stack[0]


