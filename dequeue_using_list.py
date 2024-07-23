class Dequeue:
    def __init__(self):
        self.items = []

    def is_Empty(self):
        return len(self.items) == 0
    
    def enqueue_from_front(self,data):
        print(f'{data} inserted in Dequeue')
        self.items.insert(0,data)

    def enqueue_from_rear(self,data):
        print(f'{data} inserted in Dequeue')
        self.items.append(data)
    
    def dequeue_from_rear(self):
        if not self.is_Empty():
            print(f'{self.items[-1]} element deleted from Dequeue front')
            self.items.pop()
        else:
            print('Dequeue is Empty')

    def dequeue_from_front(self):
        if not self.is_Empty():
            print(f'{self.items[0]} element deleted from Dequeue front')
            self.items.pop(0)
        else:
            print('Dequeue is Empty')

    def get_front(self):
        if not self.is_Empty():
            print(f'{self.items[0]} front element of Dequeue')
        else:
            print('Dequeue is Empty')

    def get_rear(self):
        if not self.is_Empty():
            print(f'{self.items[-1]} rear element of Dequeue')
        else:
            print('Dequeue is Empty')

    def size(self):
        print(f'{len(self.items)} total element in Dequeue')

dequeue = Dequeue()
dequeue.enqueue_from_front(10)
dequeue.enqueue_from_rear(100)
dequeue.enqueue_from_front(5)
dequeue.get_front()
dequeue.get_rear()
dequeue.size()
dequeue.enqueue_from_front(2)
dequeue.enqueue_from_rear(200)
dequeue.get_front()
dequeue.get_rear()
dequeue.size()
dequeue.dequeue_from_front()
dequeue.get_front()
