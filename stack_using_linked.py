class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self,head=None):
        self.head=head

    def is_Empty(self):
        if self.head==None:
            print('No Element in stack')
            return True
        
    def push(self,data):
        newNode = Node(data=data,next=self.head)
        self.head = newNode
        # if not self.is_Empty():
        #     newNode.next = self.head
        #     self.head=newNode
        # else:
        #     self.head = newNode

    def pop(self):
        if not self.is_Empty():
            print(f'{self.head.data} is popped')
            self.head = self.head.next
            # if self.head.next == None:
            #     print(f'{self.head.data} is popped')
            #     self.head = None
            # else:
            #     print(f'{self.head.data} is popped')
            #     self.head = self.head.next 
        else:
            pass
    

    def peek(self):
        if not self.is_Empty():
            print(f'{self.head.data} is topmost data')
        else:
            pass
    
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count+=1
            current = current.next
        print(f'Total elements stack have {count}')

# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.peek()
# stack.size()
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# stack.size()
# # stack.pop()
# stack.peek()