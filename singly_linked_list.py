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
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next


class linked_list:

    def __init__(self,head = None):
        self.head = head

    def insert_at_beg(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_last(self,data):
        newnode = Node(data)
        current = self.head
        while(current.next):
            current = current.next
        current.next = newnode

ll = linked_list()
ll.insert_at_beg(10)
ll.insert_at_beg(20)
ll.insert_at_last(100)

current = ll.head
while current:
    print(current.data)
    current = current.next

    