from  singly_linked_list import *           #Sll

class Stack(Sll):
    def __init__(self):
        super().__init__()          #this is important if you create init method in class then you need to explicitly call parrent init method
        self.item_count =0

    def is_Empty(self):
        return self.isEmpty()                #return super().isEmpty()
    
    def push(self,data):
        self.insertion_at_beg(data)         #as there is no insertion_at_beg function in child class
        self.item_count +=1

    def pop(self):
        if not self.is_Empty():
            self.deletion_at_beg()
            self.item_count-=1
        else:
            pass
    def peek(self):
        if not self.is_Empty():
            data = self.head.data
            print(f'Topmost element in stack is {data}')
        else:
            pass

    def size(self):
        print(f'Total elements in stack is {self.item_count}')


stack = Stack()
stack.is_Empty()
stack.push(1)
stack.push(2)
stack.push(3)
stack.peek()
stack.pop()
stack.peek()