#Basic Structure
    # class Node:

    #     def __init__(self,item = None,next = None):     #creating a single node
    #         self.item = item
    #         self.next = next 


#Opertions on Songly Liked list
    # -> Insertion
    #     -> insertion at beginning
    #     -> insertion at last
    #     -> insertion after specific node

    # -> Deletion
    #     -> Deletion at begining
    #     -> deletion at last
    #     -> deletion of specific node

    # -> Is_empty()

    # -> traverse


class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Sll:
    def __init__(self,head=None):
        self.head = head

    def isEmpty(self):
        if self.head == None:
            return True

    def insertion_at_beg(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertion_at_last(self,data):
        current = self.head
        while(current.next != None):
            current = current.next
        newNode  = Node(data)
        current.next = newNode

    def insertion_after_specific(self,data,after = None):
        if self.head == None:
            print('List is empty')
            return 
        current = self.head

        while current is not None:
            if current.data == after:
                newNode = Node(data,current.next)
                current.next = newNode
                print(f'node inserted with data {data} after {after}')
                return
            current=current.next
        
        print('node with element not present')
        
        # while(current!=None and current.data != after):     #first check node with data present or not,if node not present current == None
        #     current = current.next
        
        # if current == None:                                 #Check current == None  means node with data is node present and return 
        #     print(f'Node not present with data {after}')
        #     return
        
        # newnode = Node(data)                                #otherwise create new node and enter data
        # newnode.next = current.next
        # current.next = newnode

    def deletion_at_beg(self):
        if self.head ==None:
            print('list is already empty')
            return
        # self.head = self.head.next            //just by this we can handle all the cases
        current = self.head
        if current.next == None:
            print(f"deleted node is {current.data}")
            self.head = None
            return
        print(f"deleted node is {current.data}")
        nextnode = current.next
        self.head = nextnode

    def deletion_at_last(self):
        if self.isEmpty():
            print('list is empty under deletion at last')
            return
        
        elif self.head.next == None:
            self.head = None

        else:
            current = self.head
            while (current.next.next != None):
                current = current.next
            current.next = None
        
        # current = self.head
        # oneahead = self.head.next
        # if current.next == None:
        #     self.head = None
        #     return
        
        # while(oneahead.next!=None):
        #     current = current.next
        #     oneahead = oneahead.next
        # current.next = None

    def deletion_at_spec(self,data):
        if self.isEmpty():
            print('List is Empty under deletion at specific')
            return
        
        elif self.head.data == data:
            self.head = self.head.next
            return 
        else:
            current = self.head
            while current.next is not None:
                if current.next.data == data:
                    current.next = current.next.next
                    print(f'deleted node')
                    return
                current = current.next
        
            print(f'Node with data {data} is not present in list')


    def display(self):
        if self.head == None:
            print('List is empty')
            return
        current = self.head
        while (current):
            print(current.data)
            current = current.next

ll = Sll()
ll.insertion_at_beg(10)
ll.insertion_at_beg(5)
ll.insertion_at_beg(2)
ll.insertion_at_last(15)
ll.insertion_at_last(20)
ll.insertion_after_specific(12,10)
ll.insertion_after_specific(17,15)
ll.insertion_after_specific(19,17)
ll.insertion_after_specific(111,18)
print('before deletion')
ll.display()
# ll.deletion_at_beg()
# ll.deletion_at_beg()
# print('after deletion')
# print('deleting last Element')
# ll.deletion_at_last()
ll.deletion_at_spec(10)
print('after deleting')
ll.display()
ll.insertion_after_specific(21,20)
ll.display()
