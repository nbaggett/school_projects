from queue import *
from tkinter import *
import turtle

class BinarySearchTree:

    class Node:
        def __init__(self,val,left=None,right=None,x=None,y=None):
            self.val = val
            self.left = left
            self.right = right
            self.x = x
            self.y = y

        def getVal(self):
            return self.val

        def setVal(self,newval):
            self.val = newval

        def getLeft(self):
            return self.left

        def getRight(self):
            return self.right

        def setLeft(self,newleft):
            self.left = newleft

        def setRight(self,newright):
            self.right = newright

        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem

            yield self

            if self.right != None:
                for elem in self.right:
                    yield elem
        
            

        def __repr__(self):
            return "BinarySearchTree.Node(" + repr(self.val) + "," + repr(self.left) + "," + repr(self.right) + ")"            

    def __init__(self, contents=[]):
        self.root = None
      
        for item in contents:
            self.insert((item))

    def insert(self,val):
        self.root = BinarySearchTree.__insert(self.root,val)

    def __insert(root,val):
        if root == None or root.val == None:
            return BinarySearchTree.Node(val)

        if val < root.getVal():
            root.setLeft(BinarySearchTree.__insert(root.getLeft(),val))
        else:
            root.setRight(BinarySearchTree.__insert(root.getRight(),val))

        return root
    
    def __contains__(self, item):
        for node in self:
            if node.val == item:
                return True
        return False

    def __iter__(self):
        if self.root != None:
            return iter(self.root)
        else:
            return iter([])

    def __str__(self):
        return "BinarySearchTree(" + repr(self.root) + ")"
    
    def preorder(self):
        root = self.root
        lst = []
        def __preorder(root):
            
            if root.val != None:
                lst.append(root.val)
        
            if root.left != None:
                __preorder(root.left)
        
            if root.right != None:
                __preorder(root.right)
        
            return lst  
        
        return __preorder(root)          
    
    def postorder(self):
        root = self.root
        lst = []
        def __postorder(root):
            if root.left != None:
                __postorder(root.left)
                
            if root.right != None:
                __postorder(root.right)
            
            if root.val != None:   
                lst.append(root.val)
            
            return lst
        
        return __postorder(root)
                
    def inorder(self):
        lst = []
        for node in self:
            if node.val != None:
                lst.append(node.val)
        return lst
        
    def delete(self, item):
        
        def getRightMost(node):
            if node.right == None:
                return node
            else:
                return getRightMost(node.right)

        def getParent(tree, child):
            for node in tree:
                if node.right != None:
                    if node.right.val == child.val:
                        return node
                if node.left != None:
                    if node.left.val == child.val:
                        return node
            return tree.root
            
        for node in self:
            if node.val == item:
                
                #Case 1: no children
                if node.left is None and node.right is None:
                    node.setVal(None)
                    node = None
                    
                #Case 2: only one child
                elif (node.left is None and node.right is not None) or (node.left is not None and node.right is None):
                    if node.left is not None:
                        p = getParent(self, node)
                        if p != node:
                            if p.left != None and p.left.val == node.val:
                                p.left = node.left
                            elif p.right != None and p.right.val == node.val:
                                p.right = node.left
                        else:
                            self.root = node.left
                        
                    elif node.right is not None:
                        p = getParent(self, node)
                        if p != node:
                            if p.left != None and p.left.val == node.val:
                                p.left = node.right
                            elif p.right != None and p.right.val == node.val:
                                p.right = node.right
                        else:
                            self.root = node.right
         
                #Case 3: two children
                elif (node.left is not None and node.right is not None):
                    right = getRightMost(node.left)
                    node.val = right.val
                    right.val = None
            
    def levelorder(self):
        root = self.root
        lst = []
        q = Queue()
        
        def __levelorder(root):
            q.enqueue(root)
            while q.isEmpty() != True:
                x = q.dequeue()
                if x.getVal() != None:
                    lst.append(x.getVal())
                if x.getLeft() != None:
                    q.enqueue(x.left)
                if x.getRight() != None:
                    q.enqueue(x.right)
                    
        __levelorder(root)
        return lst
 
#gets height at current node, height from root is total height of tree       
def height(node):
    if node is None or node.val == None:
        return 0
    else:
        leftheight = height(node.left) 
        rightheight = height(node.right)
        
    if leftheight > rightheight:
        return leftheight+1
    else:
        return rightheight+1
    
i = 0
def knuth_layout(node, depth):
    global i
    if node.getLeft() != None and node.getLeft().getVal() != None:
        knuth_layout(node.getLeft(), depth-1)
    node.x = i
    node.y = depth
    i += 1
    if node.getRight() != None and node.getRight().getVal() != None:
        knuth_layout(node.getRight(), depth-1) 

def getParent(tree, child):
    for node in tree:
        if node.right != None:
            if node.right.val == child.val:
                return node
        if node.left != None:
            if node.left.val == child.val:
                return node
    return tree.root

        
def main():
                
    def initTk():
        def insert():
            value = theirnode.get()
            try:
                if float(value) in tree:
                    theirnode.delete(0, END)
                    return
            except:
                theirnode.delete(0, END)
                return
            try:          
                tree.insert(float(value))
            except:
                theirnode.delete(0, END)
                return
            
            theirnode.delete(0, END)
            
            t.clear()
            
            knuth_layout(tree.root, height(tree.root))
            
            for node in tree:
                drawnode(node)
                
        def remove():
            value = theirnode.get()
            try:          
                tree.delete(float(value))
            except:
                theirnode.delete(0, END)
                return
            
            theirnode.delete(0, END)
            
            t.clear()
            
            knuth_layout(tree.root, height(tree.root))
            
            for node in tree:
                drawnode(node)            

        def popupmsg(msg):
            popup = Tk()
            
            popup.title("Contains?")
            label = Label(popup, text=msg, height = 5, width = 50)
            label.pack()
            
            popup.mainloop()        
            
        def contains():
            try:
                value = float(theirnode.get())
            except:
                return
            theirnode.delete(0, END)
            if value in tree:
                popupmsg("The tree contains your value!")
            else:
                popupmsg("The tree does not contain your value.")
                
        def scaling(tree):
            l = 0
            for node in tree:
                l += 1
            if l < 3:
                return 250
            elif l < 4:
                return 150
            elif l < 5:
                return 100
            elif l < 7:
                return 75
            else:
                return 50
                
        def drawnode(node):
            scale = scaling(tree)
            if node.val != None:
                parent = getParent(tree, node)
                
                t.penup()
                t.goto((parent.x-tree.root.x)*scale, (parent.y-tree.root.y)*scale+250)
                t.pendown()
                
                t.goto(((node.x-tree.root.x)*scale), (node.y-tree.root.y)*scale+250)
                t.dot()
                t.penup()
                t.write(node.val, font=(14))
                
        window = Tk()
        
        window.title("Binary Tree Visualization")
        
        cv = Canvas(window, width=800, height=800, bg = 'white')
        cv.pack(side = LEFT)
        
        t = turtle.RawTurtle(cv)
        t.pencolor("#000000")
        t.speed(0)
        t.ht()
        
           
        frame = Frame(window, bg='light grey')
        frame.pack(side = RIGHT, fill = BOTH) 
        
        #quit button
        quit = Button(frame, text='Quit', command=window.destroy, bg = 'light grey')
        quit.pack()
        
        #node text
        entry = Label(frame, text = 'Node Value:', bg = 'light grey')
        entry.pack()
        
        #node entry box
        theirnode = Entry(frame)
        theirnode.pack()
        
        #insert button
        insertButton = Button(frame, text = 'Insert', bg = 'light grey', command = insert)
        insertButton.pack()
        
        #remove button
        removeButton = Button(frame, text = 'Remove', bg = 'light grey', command = remove)
        removeButton.pack()
        
        #contains button
        containsButton = Button(frame, text = 'Contains?', bg = 'light grey', command = contains)
        containsButton.pack()
        
        window.mainloop()      
        
    tree = BinarySearchTree()
    initTk()
    
    
if __name__ == "__main__":
    main()