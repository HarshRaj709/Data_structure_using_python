class Queue(list):
    def is_Empty(self):
        return len(self)==0
    def enqueue(self,data):
        print(f'{data} is enqueued in Queue')
        self.append(data)
    def dequeue(self):
        if not self.is_Empty():
            print(f'data {self[0]} is dequeued')
            self.pop(0)
        else:
            print('Queue is Empty')
    def get_front(self):
        if not self.is_Empty():
            print(f'Front data is {self[0]}')
        else:
            print('Queue is Empty')
    def get_rear(self):
        if not self.is_Empty():
            print(f'Rear data is {self[-1]}')
        else:
            print('Queue is Empty')
    def size(self):
        print(f'size of queue is {len(self)}')

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.size()
queue.get_front()
queue.get_rear()
queue.dequeue()
queue.get_front()
queue.get_rear()