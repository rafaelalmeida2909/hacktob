
class Stack():
    """A simple stack in python"""
    def __init__(self, lenght) -> None:
        self.stack = []
        self.lenght = lenght # max stack's lenght

    def push(self, elem: str) -> None:
        if len(self.stack) < self.lenght:
            self.stack.append(elem)
        else:
            print("stack_is_full")

    def pop(self) -> str:
        if len(self.stack) > 0:
            return self.stack.pop()
        print("stack_is_empty")

    def __len__(self) -> int:
        return len(self.stack)
