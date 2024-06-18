from collections import deque
class MyStack:
    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()
    def push(self, x: int) -> None:
        self.stack1.append(x)
    def pop(self) -> int:
        while len(self.stack1) > 1:
            temp = self.stack1.popleft()
            self.stack2.append(temp)     
        if len(self.stack1) == 1:
            answer = self.stack1.popleft()
            self.stack1, self.stack2 = self.stack2, self.stack1
        return answer
    def top(self) -> int:
        return self.stack1[-1]
    def empty(self) -> bool:
        return False if self.stack1 else True
