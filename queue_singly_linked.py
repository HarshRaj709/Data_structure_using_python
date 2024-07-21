class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.item_count = 0
        self.front = None
        self.rear = None

    def is_Empty(self):
        return self.front==None
    
    def enqueue(self,data):
        newNode = Node(data=data)
        if not self.is_Empty():
            # newNode.next = self.rear.next
            self.rear.next = newNode
            self.rear = newNode
        else:
            self.front = self.rear = newNode
        self.item_count += 1

    def dequeue(self):
        if not self.is_Empty():
            data = self.front.data
            if self.item_count == 1:            #self.front == self.rear:
                # print(f'{self.front.data} is deleted')
                self.front = self.rear = None
            else:
                # print(f'{self.front.data} is deleted')
                self.front = self.front.next
            print(f'{data} is deleted')
            self.item_count -=1
        else:
            print('No item in Queue')

    def get_front(self):
        if not self.is_Empty():
            print(f'Front is {self.front.data}')
        else:
            print('No item in Queue')

    def get_rear(self):
        if not self.is_Empty():
            print(f'Rear is {self.rear.data}')
        else:
            print('No item in Queue')

    def size(self):
        print(f'Total Elements in Queue are {self.item_count}')

queue = Queue()
print(queue.is_Empty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.size()
queue.get_front()
queue.get_rear()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.size()
queue.get_front()
queue.get_rear()