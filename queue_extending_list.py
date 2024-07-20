from singly_linked_list import *

class Queue:
    def __init__(self):
        self.myqueue = Sll()

    def is_Empty(self):
        self.myqueue.isEmpty()

    def enqueue(self,data):
        self.myqueue.insertion_at_last(data)

    def dequeue(self):
        if not self.is_Empty():
            print(f'Data with {self.myqueue.head.data}')
            self.myqueue.deletion_at_beg()
        else:
            print('Queue is empty')

    def get_first(self):
        if not self.is_Empty():
            print(f'First data is {self.myqueue.head.data}')
        else:
            print('Queue is empty')
    
    def get_rear(self):
        if not self.is_Empty():
            current = self.myqueue.head
            while current.next != None:
                current = current.next
            print(f'Rear item is {current.data}')

    def size(self):
        count = 0
        current = self.myqueue.head
        while current != None:
                count +=1
                current = current.next
        print(f'Total size is {count}')

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.size()        # Output: Total size is 3
queue.get_first()   # Output: First data is 1
queue.get_rear()    # Output: Rear item is 3
queue.dequeue()     # Output: Dequeued data: 1
queue.size()        # Output: Total size is 2
queue.get_first()   # Output: First data is 2
queue.get_rear()