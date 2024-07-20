from singly_linked_list import *

class Queue(Sll):           #child of singly linked list thats why it have acess to all methods of sll
    def __init__(self):
        super().__init__()
    
    def is_Empty(self):
        self.isEmpty()
    
    def enqueue(self,data):
        self.insertion_at_last(data)

    def dequeue(self):
        if not self.is_Empty():
            self.deletion_at_beg()
        else:
            pass
    def get_front(self):
        if not self.is_Empty():
            print(f'First item is {self.head.data}')
        else:
            pass
    def get_rear(self):
        if not self.is_Empty():
            current = self.head
            while current.next != None:
                current = current.next
            print(f'Rear item is {current.data}')

    def size(self):
        count = 0
        current = self.head
        while current != None:
                count +=1
                current = current.next
        print(f'Total size is {count}')
    
    def deletion_at_last(self):
        raise AttributeError('Not allowed in Queue')

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.get_front()
queue.get_rear()
queue.size()
queue.dequeue()
queue.get_front()
queue.size()
try:
    queue.deletion_at_last()         #it can be use to save that you can override it
except AttributeError as e:
    print(e)
queue.size()

