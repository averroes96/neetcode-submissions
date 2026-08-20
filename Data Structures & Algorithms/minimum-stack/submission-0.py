class MinStack:

    def __init__(self):
        self.elements = []

    def push(self, val: int) -> None:
        try:
            int(val)
            self.elements.append(val)
        except ValueError:
            self.elements.append(None)

    def pop(self) -> None:
        self.elements.pop()

    def top(self) -> int:
        return self.elements[-1]

    def getMin(self) -> int:
        return min(self.elements)
        
