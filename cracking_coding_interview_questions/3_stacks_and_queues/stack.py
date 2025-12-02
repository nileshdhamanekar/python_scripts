class Stack:
    def __init__(self):
        self.my_stack = list()

    def push(self, item):
        self.my_stack.append(item)

    def pop(self):
        if len(self.my_stack) < 1:
            return None
        else:
            return self.my_stack.pop()

    def print_stack(self):
        print(self.my_stack)


stack = Stack()
stack.print_stack()
stack.push(14)
stack.print_stack()
stack.push(43)
stack.print_stack()
stack.push(573)
stack.print_stack()
stack.pop()
stack.print_stack()
stack.pop()
stack.print_stack()
stack.push("fssgae")
stack.print_stack()
stack.pop()
stack.print_stack()