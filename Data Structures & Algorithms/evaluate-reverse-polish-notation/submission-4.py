class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        result = None

        def do_math(first, second, operator):
            match(operator):
                case "+": return int(first + second)
                case "-": return int(first - second)
                case "*": return int(first * second)
                case "/": return int(first / second)

        for token in tokens:
            try:
                stack.append(int(token))
            except:
                first = stack.pop(-2)
                second = stack.pop(-1)
                result = do_math(first, second, token)
                stack.append(result)
        
        return stack[0]


