class Stack(object):
    def __init__(self, limit = 10):
        self.stk = []
        self.limit = limit
    def isEmpty(self):
        if len(self.stk) <= 0:
            return 0
    def push(self, item):
        if (len(self.stk) >= self.limit):
            print("stack is full")
        else:
            self.stk.append(item)
            print(self.stk)
    def pop(self):
        if len(self.stk) <= 0:
            print("Stack Underflow")
        else:
            self.stk.pop()
            print(self.stk)
    def peek(self):
        if len(self.stk) != 0:
            print(self.stk[-1])
    def size(self):
        print(len(self.stk))
if __name__ == "__main__":
    my_stack = Stack(10)
    my_stack.push(34)
    my_stack.push(23)
    my_stack.push(22)
    my_stack.peek()
    my_stack.pop()
    my_stack.peek()
                