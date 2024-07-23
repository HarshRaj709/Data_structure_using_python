class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.prev = prev
        self.data = data
        self.next = next

class Dequeue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_Empty(self):
        return self.front == None           #self.item_count == 0
    
    def enqueue_front(self,data):
        newNode = Node(data=data,next = self.front)
        if not self.is_Empty():
            self.front.prev = newNode    
        else:
            self.rear = newNode
        self.front = newNode 
        self.item_count += 1

    def enqueue_rear(self,data):
        newNode = Node(prev=self.rear,data=data)
        if not self.is_Empty():
            self.rear.next=newNode
        else:
            self.front = newNode
        self.rear = newNode 
        self.item_count += 1

    def dequeue_front(self):
        if not self.is_Empty():
            if self.front == self.rear:
                self.front = self.rear = None
            else:
                self.front = self.front.next
                self.front.prev = None
            self.item_count -=1
        else:
            print('no element to delete')

    def dequeue_rear(self):
        if not self.is_Empty():
            if self.front==self.rear:
                self.front = self.rear =None
            else:
                self.rear = self.rear.prev
                self.rear.next = None
            self.item_count -= 1
        else:
            print('no element to delete')

    def get_front(self):
        if not self.is_Empty():
            print(f'{self.front.data} is front element')
        else:
            print('No element in dequeue')

    def get_rear(self):
        if not self.is_Empty():
            print(f'{self.rear.data} is front element')
        else:
            print('No element in dequeue')

    def size(self):
        print(f'{self.item_count} is total length of queue')

dequeue = Dequeue()
dequeue.enqueue_front(10)
dequeue.enqueue_rear(100)
dequeue.enqueue_front(5)
dequeue.size()
dequeue.get_front()
dequeue.get_rear()
dequeue.dequeue_front()
dequeue.get_front()

