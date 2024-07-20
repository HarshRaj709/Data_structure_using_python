from singly_linked_list import *


class Stack:
    def __init__(self):
        self.mylist = Sll()     #created object of sll
        self.item_count = 0

    def is_Empty(self):
        return self.mylist.isEmpty()
    
    def push(self,data):
        self.mylist.insertion_at_beg(data)
        self.item_count+=1

    def pop(self):
        if not self.is_Empty():
            self.mylist.deletion_at_beg()
            self.item_count -= 1
        else:
            pass

    def peek(self):
        if not self.is_Empty():
            data = self.mylist.head.data
            print(f'topmost data is {data}')
        else:
            pass

    def size(self):
        print(f'Stack have {self.item_count} elements')


stack = Stack()
stack.is_Empty()
stack.push(1)
stack.push(2)
stack.push(3)
stack.size()
stack.peek()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.peek()
stack.size()


