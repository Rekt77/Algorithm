import sys
sys.setrecursionlimit(20_000)
class node:
    def __init__(self,v=None,left=None,right=None):
        self.v = v
        self.left = left
        self.right = right

class BST():
    def __init__(self):
        self.root = None

    def insertNode(self,num):
        if self.root == None:
            self.root = node(num)
        else:
            self.__insert_node(node(num),self.root)
    
    def __insert_node(self,node,cur):
        if cur.v>node.v:
            if cur.left==None:
                cur.left = node
            else:
                self.__insert_node(node,cur.left)
        else:
            if cur.right==None:
                cur.right = node
            else:
                self.__insert_node(node,cur.right)

    def postorder_traverse(self): 
        if self.root is not None:
            self.__postorder(self.root)
    def __postorder(self,cur):
        if cur.left is not None:
            self.__postorder(cur.left)
        if cur.right is not None:
            self.__postorder(cur.right)
        print(cur.v)

#lis = [50,30,24,5,28,45,98,52,60]

myTree = BST()
count = 0
while count <= 10000:
    try:
        myTree.insertNode(int(input()))
    except:
        break
    count+=1

myTree.postorder_traverse()

