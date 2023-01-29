import unittest
import bst

class TestBST(unittest.TestCase):
    # Creating a dummy list of 3 elements
    def setUp(self):
        self.my_tree = bst.BST()
        self.my_tree.add(5)
        self.my_tree.add(7)
        self.my_tree.add(3)

    def test_append_new(self):
        self.assertTrue(self.my_tree.size == 3)
        self.assertTrue(self.my_tree.head.val == 5)
        self.assertTrue(self.my_tree.head.left.val == 3)
        self.assertTrue(self.my_tree.head.left.right == 7)

if __name__ == '__main__':
    unittest.main()