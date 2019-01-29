from binarytreevis import *
import unittest

class Asg3Tests(unittest.TestCase):
    # INSTRUCTOR UNIT TESTS
    def test_binsearchtree_constructor1(self):
        bt1 = BinarySearchTree( contents=[0, 1, 2, 5, 90, -1] )
        bt2 = BinarySearchTree( contents=[0, 1, 2, 5, 90, -1] ) 

        self.assertListEqual( bt1.inorder(), bt2.inorder() )
        self.assertListEqual( bt1.preorder(), bt2.preorder() )
        self.assertListEqual( bt1.postorder(), bt2.postorder() )
        self.assertListEqual( bt1.levelorder(), bt2.levelorder() )

    def test_binsearchtree_inorder1(self):
        bt = BinarySearchTree(contents=[0, -1, 1]) 
        self.assertListEqual(bt.inorder(), [-1, 0, 1]) 

    def test_binsearchtree_preorder1(self):
        bt = BinarySearchTree( contents=[2, 0, 1] )
        self.assertListEqual( [2, 0, 1], bt.preorder() )

    def test_binsearchtree_postorder1(self):
        bt = BinarySearchTree( contents=[2, 0, 1] )
        self.assertListEqual( [1, 0, 2], bt.postorder() ) 

    def test_binsearchtree_levelorder1(self):
        bt = BinarySearchTree( contents=[2, 0, 1, 6, 10] ) 
        self.assertListEqual( [2, 0, 6, 1, 10], bt.levelorder() )  

    def test_binsearchtree_insert1(self):
        bt = BinarySearchTree() 
        bt.insert(0); bt.insert(-1); bt.insert(1)
        self.assertListEqual(bt.inorder(), [-1, 0, 1])    

    def test_binsearchtree_delete1(self):
        bt = BinarySearchTree(contents=[0, 1, 2]) 
        bt.delete(0)
        self.assertListEqual(bt.inorder(), [1, 2])

    def test_binsearchtree_contains1(self):
        bt = BinarySearchTree(contents=[0, 1, 2]) 
        self.assertTrue(0 in bt)    
        bt.delete(0)
        self.assertFalse(0 in bt)
        
    # STUDENT PROGRAMMER UNIT TESTS FOR ADDED FUNCTIONS
    def test_binsearchtree_height1(self):
        bt = BinarySearchTree(contents=[0, -1, 1])
        h = height(bt.root)
        self.assertEqual(h, 2)
    
    def test_binsearchtree_height2(self):
        bt = BinarySearchTree(contents=[0, -1, 1, 2, 3])
        h = height(bt.root)
        self.assertEqual(h, 4) 
        
    def test_binsearchtree_getparent1(self):
        bt = BinarySearchTree(contents=[0, -1, 1, 2, 3])
        child = bt.root.left
        parent = getParent(bt, child)
        self.assertEqual(parent.val, bt.root.val)
    
    def test_node_xyvals(self):
        bt = BinarySearchTree(contents=[0, -1, 1, 2])
        knuth_layout(bt.root, height(bt.root))
        self.assertEqual(bt.root.left.x, 0)
        self.assertEqual(bt.root.x, 1) 
        self.assertEqual(bt.root.y, height(bt.root))
        self.assertEqual(bt.root.left.y, 2)
    
if __name__ == '__main__':
    unittest.main()
