class Stack(list):
    def isEmpty(self):
        return len(self)==0         #True is size is empty, we use self only because stack is child of list and we can access it by self.
    
    def push(self,data):
        self.append(data)
        print(f'Data pushed {data}')

    def pop(self):
        if not self.isEmpty():
        #self.pop()      #we cant use it directly as it will cause recursion, because of overriding method pop
            print(f'{super().pop()} data is popped')
        else:
            print('stack is empty')

    def peek(self):
        if not self.isEmpty():
            print(f'top most data is {self[-1]}')
        else:
            print('stack is empty')

    def size(self):
        if not self.isEmpty():
            print(f'there are {len(self)} items in stack')
        else:
            print('stack is empty')

    def insert(self,index,data):
        raise AttributeError("Sorry you can't use insert method in Stack")



stack = Stack()
print(stack.isEmpty())
stack.push(1)
stack.push(2)
stack.size()
stack.peek()
stack.pop()
# stack.insert(2,10)            #i dont want that to run as this is not allowed in stack
stack.peek()