class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items)==0:
            print('stack is Empty')
            return True
        else:
            return False
            # print('list is empty')
            # return

    def push(self,data):
        self.items.append(data)

    def pop(self):
        if self.isEmpty():
            # print('no item in stack')
            return
        data = self.items.pop()
        print(f'data on top is {data}')
    
    def peek(self):
        if self.isEmpty():
            # print('no item in stack')
            return
        peek = self.items[-1]
        print(f'top most item is {peek}')

    def size(self):
        print(f'{len(self.items)} items in the stack')

stack = Stack()
# stack.isEmpty() #True
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.peek()
# stack.size()
stack.pop()
# stack.size()