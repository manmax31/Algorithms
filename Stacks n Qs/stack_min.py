# Design a stack that has O(1) push, pop and min functions


class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack(object):
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    @property
    def pop(self):
        self.top = self.top.next
        # self.display()

    @property
    def is_empty(self):
        return self.top is None

    @property
    def peek(self):
        return self.top.data

    def display(self):
        runner = self.top
        while runner:
            print(runner.data, end='')
            print('->', end='')
            runner = runner.next
        print(None)


class StackWithMin2(object):
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x):
        self.stack.insert(0, x)
        if not self.min or x <= self.get_min():
            self.min.insert(0, x)

    def pop(self):
        x = self.stack.pop(0)
        if x == self.get_min():
            self.min.pop(0)
        return x

    def get_min(self):
        return self.min[0]

    def display(self):
        print(self.stack)

if __name__ == "__main__":
    print("Normal LIFO Stack")
    s = Stack()
    s.push(3)
    s.push(5)
    s.push(2)
    s.push(7)
    s.push(1)
    s.push(10)
    s.push(0)
    s.display()
    print("Top of Stack is: ", s.peek)
    print('After poping 2 times:')
    s.pop
    s.pop
    s.display()

    print("\n\nGetting Min of Stack in O(1):")
    s = StackWithMin2()
    s.push(3)
    s.push(5)
    s.push(2)
    s.push(7)
    s.push(1)
    s.push(10)
    s.push(0)
    s.display()
    print('Min of Stack is:', s.get_min())
    s.pop()

    print("\nAfter popping 1 times")
    s.display()
    print('Min of Stack is:', s.get_min())
    s.pop()
    s.pop()

    print("\nAfter popping 2 more times")
    s.display()
    print('Min of Stack is:', s.get_min())



