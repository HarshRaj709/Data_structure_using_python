class Node:
    def __init__(self,prev=None,data = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next

class DLL:
    def __init__(self,head = None):
        self.head = head

    def insertion_at_beg(self,data):
        newnode = Node(data=data ,next = self.head)
        if self.head is not None:
            self.head.prev = newnode
        self.head = newnode
        # if self.head == None:
        #     self.head = newnode
        # else:
        #     current = self.head
        #     current.prev = newnode
        #     newnode.next = self.head
        #     self.head = newnode

    def insertion_at_last(self,data):
        current = self.head
        newNode = Node(data = data)
        if self.head is None:
            self.head = newNode
            return
        
        while current.next:
            current = current.next
        current.next = newNode
        newNode.prev = current


    def insertion_after_spec(self,data,after=None):
        current = self.head
        newNode = Node(prev = current ,data=data)
        
        while current is not None:
            if current.data == after:
                newNode.next = current.next
                newNode.prev = current
                if current.next:
                    current.next.prev = newNode
                current.next = newNode
                print(f'Node {data} added after node {after}')
                return
            current = current.next
        print(f'Node with data {after} not present in the list')
            #  while current is not None:
            #     if current.data == after:
            #        if current.next is not None:
            #            current.next.prev = newNode
            #        newNode.next = current.next
            #        current.next = newNode
            #        print(f'Node {data} added after node {after}')
            #        return
            #     current = current.next

            # print(f'Node with data {after} not presented in the list')

    def deletion_at_beg(self):
        if self.head is None:
            print('list is empty')
            return
        
        current = self.head
        print(f'Node with {current.data} is deleted')
        self.head = current.next
        current.prev = None

    def deletion_at_last(self):
        current = self.head
        if self.head is not None:
            if current.next is None:
                print(f'Node with {current.data} is deleted')
                self.head = None
                return
            else:
                while current.next.next:
                    current = current.next
                print(f'Node with {current.next.data} is deleted')
                current.next = None
        else:
            print('List is Empty')
                

    def deletion_of_specific(self, data):
        current = self.head
        # If list is empty
        if self.head is None:
            print('List is empty')
            return
        
        # If node to be deleted is head node
        if current.data == data:
            if current.next is None:
                self.head = None
            else:
                self.head = current.next
                self.head.prev = None
            print(f"Node deleted with data {data}")  
            return

        # Traverse the list to find the node with the given data
        while current is not None and current.data != data:
            current = current.next

        # If node not found
        if current is None:
            print(f'Node not found with data {data}')
            return
        
        # If node to be deleted is the last node
        if current.next is None:
            current.prev.next = None
            print(f"Node deleted with data {data}")
            return
        
        # If node to be deleted is in the middle
        current.prev.next = current.next
        current.next.prev = current.prev
        print(f"Node deleted with data {data}")        
        


    def display(self):
        if self.head == None:
            print('List contains Null')
            return
        
        current = self.head
        while(current!=None):
            print(current.data)
            current = current.next

dll = DLL()
dll.insertion_at_beg(10)
dll.insertion_at_beg(8)
dll.insertion_at_beg(6)
dll.insertion_at_last(11)
dll.insertion_at_last(12)
dll.insertion_at_last(14)
# dll.insertion_after_spec(13,12)
# dll.insertion_after_spec(15,14)
# dll.insertion_after_spec(15,18)
dll.display()
# dll.deletion_at_beg()
# dll.deletion_at_beg()
# dll.deletion_at_last()
dll.deletion_of_specific(11)
dll.display()
