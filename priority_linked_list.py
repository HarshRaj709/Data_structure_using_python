class Node:
    def __init__(self,data=None,priority=None,next=None):
        self.data = data
        self.priority = priority
        self.next = next

class PriorityQueue:
    def __init__(self,head=None):
        self.head = head
        self.item_count = 0

    def is_Empty(self):
        return self.head is None
            

    def push(self,data,priority):
        newNode = Node(data,priority)
        if not self.head or priority < self.head.priority:
            #insertion at first
            newNode.next = self.head
            self.head = newNode
        else:
            #insertion_at_mid or at the end
            current = self.head
            while current.next and current.next.priority <= priority:       #if no node found with low priority it will add at end
                current = current.next
            newNode.next = current.next
            current.next = newNode
        self.item_count +=1

    def pop(self):
        if not self.is_Empty():
            print(f'{self.head.data} is removed from queue')
            self.head = self.head.next
            self.item_count -= 1
        else:
            print('No Element in Priority queue')

    def size(self):
        print(f'{self.item_count} is the size of queue')
    

        
pri = PriorityQueue()
pri.push('amit',4)
pri.push('arjun',7)
pri.push('harsh',2)
pri.push('gunjan',5)
pri.push('samita',8)

while not pri.is_Empty():
    pri.pop()
    