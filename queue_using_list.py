class Queue:
    def __init__(self):
        self.items = []

    def is_Empty(self):
        return len(self.items)==0
    
    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_Empty():
            print(f'item with {self.items[0]} is deleted')
            self.items.pop(0)
        else:
            print('Queue is empty')
    
    def get_front(self):
        if not self.is_Empty():
            print(f'Front item is {self.items[0]}')
        else:
            print('Queue is empty')

    def get_rear(self):
        if not self.is_Empty():
            print(f'Rear item is {self.items[-1]}')
        else:
            # print('Queue is empty')
            raise IndexError('queue is Empty')

    def size(self):
        print(f'Total elements in queue are {len(self.items)}')

queue=Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# queue.size()
# queue.dequeue()
# queue.dequeue()
queue.get_front()
try:
    queue.get_rear()
except IndexError as e:
    print(e)
queue.size()