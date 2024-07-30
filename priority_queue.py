class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_Empty(self):
        return len(self.items)==0

    def push(self,data,priority):
        index = 0           #to mark indexes,    we will place most priority data to lowest index
        while index < len(self.items) and self.items[index][1]<=priority:       #means here we are entering tuples in list and checking that the tuple on index 0 must have highest priority then currently entering data's priority  
            index +=1
        print(f'{data} is pushed to queue')
        self.items.insert(index,(data,priority))

    def pop(self):
        if not self.is_Empty():
            print(f'{self.items[0][0]} is deleted')
            self.items.pop(0)
        else:
            print('Priority queue is empty')
    
    def get_front(self):
        if not self.is_Empty():
            print(f'front data is {self.items[0][0]}')
        else:
            print('queue is empty')

    def get_rear(self):
        if not self.is_Empty():
            print(f'Rear data is {self.items[-1][0]}')
        else:
            print('queue is empty')

    def size(self):
        print(f'Total length of priority queue is {len(self.items)}')

pri = PriorityQueue()
pri.push('harsh',2)
pri.push('rashmi',3)
pri.push('anuj',1)
pri.size()
pri.get_front()
pri.get_rear()
pri.push('kirti',12)
pri.get_front()
pri.get_rear()
pri.pop()
pri.get_front()
pri.get_rear()

    
