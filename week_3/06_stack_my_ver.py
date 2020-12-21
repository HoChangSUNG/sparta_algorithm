class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next=self.head
        self.head=new_head
        return

    # pop 기능 구현
    def pop(self):
        if self.head.next is None :
            self.head=None
        else :
            self.head=self.head.next

    def peek(self):
        print(self.head.data)

    # isEmpty 기능 구현
    def is_empty(self):
        if self.head == None :
            return True
        return False

stack = Stack()
stack.push(4)
stack.push(7)
stack.peek()
stack.pop()
print(stack.is_empty())
stack.peek()