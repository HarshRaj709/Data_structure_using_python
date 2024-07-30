class Node:
    def __init__(self,left=None,data=None,right=None):
        self.left = left
        self.data = data
        self.right = right

    def __repr__(self):
        return f"Node is present {self.data}"

class Bst:
    def __init__(self,root=None):
        self.root = root        #self.root = None

    
    def insertion(self,data):
        newNode = Node(data=data)
        if self.root is None:
            self.root = newNode
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = newNode
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = newNode
                    break
                current = current.right

    # def insertion(self,data):
    #     self.root = self.rinsert(self.root,data)
        
    # def rinsert(self,root,data):
    #     if root is None:
    #         return Node(data=data)
    #     if data < root.data:
    #         root.left = self.rinsert(root.left,data)
    #     elif data > root.data:
    #         root.right = self.rinsert(root.right,data)
    #     return root
    
    def search(self,data):
        current = self.root
        while current is not None and current.data != data:
            if data < current.data:
                current = current.left
            else:
                current = current.right
        return current

    # def search(self,data):
    #     return self.rsearch(self.root,data)
    
    # def rsearch(self,root,data):
    #     if root is None or root.data == data:
    #         return root 
    #     elif data < root.data:
    #         return self.rsearch(root.left,data)
    #     else:
    #         return self.rsearch(root.right,data)
        
    def inorder(self):
        result = []
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.data)
            self.rinorder(root.right,result)

    def preorder(self):
        result = []
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root:
            result.append(root.data)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)

    def postorder(self):
        result = []
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.data)



bst = Bst()
bst.insertion(12)
bst.insertion(10)
bst.insertion(23)
bst.insertion(2)
print(bst.inorder())
print(bst.preorder())
print(bst.postorder())
print(bst.search(2))

    
    


        




# newNode = Node(data= data)
#         if not self.root is None:
#             if self.root.data > data:
#                 self.root.left = newNode
#             else:
#                 self.root.right = newNode
#         else:
#             self.root = newNode