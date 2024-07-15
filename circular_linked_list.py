class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class CLL:
    def __init__(self,tail = None):
        self.tail = tail

    def insertion_at_beg(self,data):
        newNode = Node(data)
        current = self.tail
        if current is None:
            current = newNode
            current.next = newNode
            self.tail = current

        else:
            newNode.next = current.next
            current.next = newNode

    def insertion_at_last(self,data):
        newNode = Node(data)
        current = self.tail
        if current is None:
            current = newNode
            current.next = newNode
            self.tail = current
        
        else:
            newNode.next = current.next
            current.next = newNode
            self.tail = newNode

    def insertion_after_apec(self,data,after = None):
        newNode = Node(data)
        current = self.tail
        #list is empty
        if current is None:
            print('list is empty')
            return
        current = current.next  #start from head
        #inserting after tail node
        if self.tail.data == after:
            self.insertion_at_last(data)
            return
        #traverse the list and find the Node
        # while current.next != self.tail.next:
        while True:
            if current.data == after:
                newNode.next = current.next
                current.next = newNode
                return
            current = current.next
            if current == self.tail.next:
                break
        print(f'No node found with data {after}')

    def deletion_at_beg(self):
        if self.tail is not None:
            if self.tail.next == self.tail:
                print(f'Node with data {self.tail.data} is deleted')
                self.tail = None
            else:
                current = self.tail.next
                print(f'Node with data {current.data} is deleted')
                self.tail.next = current.next
        else:
            print('List is empty')
        # if self.tail is None:
        #     print('List is Empty')
        #     return
        # current = self.tail.next        #head of list

        # # when there is only 1 Node
        # if current == self.tail:
        #     self.tail = None        # List becomes empty
        #     print(f'Node with data {current.data} is deleted')
        # else:
        #     print(f'Node with data {current.data} is deleted')
        #     self.tail.next = current.next

    def deletion_at_last(self):
            if self.tail is not None:
                if self.tail.next == self.tail:
                    print(f'Node with data {self.tail.data} is deleted')
                    self.tail = None
                else:
                    current = self.tail.next
                    while current.next != self.tail:
                        current=current.next
                    print(f'Node with data {current.next.data} is deleted')
                    current.next = self.tail.next
                    self.last = current
            else:
                print('list is empty cant delete from last')

    def deletion_of_item(self,data):
        # list not Empty
        if self.tail is not None:
            # list has only 1 node
            if self.tail.next == self.tail:
                if self.tail.data == data:
                    print(f'Node with data {self.tail.data} is deleted')
                    self.tail = None
                else:
                    print(f'No node with data {data}')
            # list has multiple nodes
            else:
                #deletion of 1st node
                if self.tail.next.data==data:
                    self.deletion_at_beg()
                else:
                    # we have to delete other nodes than last node
                    current = self.tail.next

                    while current != self.tail:
                        if current.next == self.tail:
                            self.deletion_at_last()
                            return
                        # general case
                        if current.next.data == data:
                            print(f'Node with data general case {current.next.data} is deleted')
                            current.next = current.next.next
                            return
                        current = current.next
                          
        else:
            print('list is empty')


    def display(self):
        current = self.tail
        if current is None:
            print('list is empty')
            return
        
        current = self.tail.next
        # while current != self.tail:
        #     print(current.data)
        #     current = current.next
        # print(current.data)
        while True:
            print(current.data)
            current = current.next
            if current == self.tail.next:
                break
        

cll = CLL()
cll.insertion_at_beg(15)
cll.insertion_at_beg(10)
cll.insertion_at_beg(5)
cll.insertion_at_last(20)
cll.insertion_at_last(25)
cll.insertion_at_last(30)
# cll.insertion_after_apec(6,35)
# cll.display()
# cll.deletion_at_last()
# print('after deletion')
cll.display()
cll.deletion_of_item(20)
print('after deletion')
cll.display()