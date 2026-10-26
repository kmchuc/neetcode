class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_tracker = []

    def push(self, val: int) -> None:
        if self.minimum_tracker:
            minimum = min(self.minimum_tracker[-1], val)
        else:
            minimum = val
        self.minimum_tracker.append(minimum)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minimum_tracker.pop()

    def top(self) -> int:
        top = self.stack[-1]
        return top

    def getMin(self) -> int:
        return self.minimum_tracker[-1]
