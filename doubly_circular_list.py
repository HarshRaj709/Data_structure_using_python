class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.prev = prev
        self.data = data
        self.next = next

class DCLL:
    def __init__(self,head = None):
        self.head = head

    def insertion_at_beg(self,data):
        newNode = Node(data=data)
        if self.head is None:
            newNode.next = newNode
            newNode.prev = newNode
            # self.head = newNode
        else:
            current=self.head
            newNode.prev = current.prev
            newNode.next = current
            current.prev.next = newNode
            current.prev = newNode
        self.head = newNode

    def insertion_at_last(self,data):
        newNode = Node(data=data)
        if self.head is None:
            newNode.next = newNode
            newNode.prev = newNode
            self.head = newNode
        else:
            last = self.head.prev
            newNode.prev = last
            newNode.next = self.head
            last.next = newNode
            self.head.prev = newNode

    def insertion_after_spec(self,data,after=None):
        newNode = Node(data = data)
        if self.head is not None:
            #single Node case
            if self.head.next== self.head:
                if self.head.data == after:
                    self.insertion_at_last(data)
                    return
                else:
                    print(f'No node with data {after}')
            #multiple nodes
                #insert after head node
            if self.head.data == after:
                    newNode.next = self.head.next
                    newNode.prev = self.head
                    self.head.prev.next = newNode
                    self.head.next = newNode
                    return
                    
                #insert after tail node
            tail = self.head.prev
            if tail.data == after:
                self.insertion_at_last(data)
                return
                    #in mid
            current = self.head
            while True: 
                if current.data == after:
                    newNode.next = current.next
                    newNode.prev = current
                    current.next.prev = newNode
                    current.next = newNode
                    return
                current = current.next
                if current == self.head:
                    print(f'Node not found with data {after}')
                    return
        else:
            print(f'No node in the list')


    def deletion_at_beg(self):
        if self.head is not None:
            if self.head.next == self.head:
                print(f'node with data {self.head.data} is deleted.')
                self.head = None
            else:
                print(f'node with data {self.head.data} is deleted.')
                self.head.next.prev = self.head.prev
                self.head.prev.next = self.head.next
                self.head = self.head.next
        else:
            print('list is empty')
        # if self.head is None:
        #     print('list has zero node')
        #     return
        
        # if self.head.next == self.head:
        #     print(f'node with data {self.head.data} is deleted.')
        #     self.head = None
        # else:
        #     print(f'node with data {self.head.data} is deleted.')
        #     self.head.next.prev = self.head.prev
        #     self.head.prev.next = self.head.next
        #     self.head = self.head.next

    def deletion_at_last(self):
        if self.head is not None:
            if self.head.next == self.head:
                print(f'node with data {self.head.data} is deleted.')
                self.head = None
            else:
                tail = self.head.prev
                print(f'node with data {tail.data} is deleted.')
                tail.prev.next = self.head
                self.head.prev = tail.prev
        else:
            print('list is empty')

    def delete_item(self,data):
        if self.head is not None:
            if self.head.next == self.head:
                if self.head.item == data:
                    self.head = None
                else:
                    print(f'node with data {data} is not present')
                    return
            #multiple nodes
            #deletion of 1st Node
            if self.head.data == data:
                self.deletion_at_beg()
                return
            #deletion of last node
            if self.head.prev.data == data:
                self.deletion_at_last()
                return
            current = self.head
            while True:
                if current.next.data == data:
                    print(f'Node with data {data} deleted successfully.')
                    current.next = current.next.next
                    current.next.next.prev = current
                    return
                current = current.next
                if current == self.head:
                    print(f'Node not present with data {data}.')
                    return



    def display(self):
        if self.head is None:
            print('list is empty')
            return
        
        current = self.head
        while True:
            print(current.data,end=' ')
            current = current.next
            if current == self.head:
                break
        # while current.next != self.head:
        #     print(current.data)
        #     current = current.next
        # print(self.head.prev.data)
        


dcll = DCLL()
dcll.insertion_at_beg(5)
dcll.insertion_at_beg(4)
dcll.insertion_at_last(6)
dcll.insertion_at_last(7)
dcll.insertion_at_last(8)
# dcll.display()
# print()
# print('after insertion')
# dcll.insertion_after_spec(4.5,6)
# dcll.display()
# print()
# dcll.deletion_at_beg()
# dcll.deletion_at_beg()
# print()
dcll.display()
print()
dcll.delete_item(6)
dcll.display()