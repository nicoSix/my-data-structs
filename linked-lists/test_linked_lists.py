import unittest
import linked_lists

class TestSinglyLinkedList(unittest.TestCase):
    # Creating a dummy list of 3 elements
    def setUp(self):
        self.my_list = linked_lists.SinglyLinkedList()
        self.my_list.append_new(1)
        self.my_list.append_new(2)
        self.my_list.append_new(3)

    def test_append_new(self):
        self.assertTrue(self.my_list.size == 3)
        self.assertTrue(self.my_list.head.data == 1)
        self.assertTrue(self.my_list.head.next_node.data == 2)

    def test_remove_pos_first(self):
        self.my_list.remove_at_pos(0)
        self.assertTrue(self.my_list.size == 2)
        self.assertTrue(self.my_list.head.data == 2)
        self.assertTrue(self.my_list.head.next_node.data == 3)

    def test_remove_pos_last(self):
        self.my_list.remove_at_pos(2)
        self.assertTrue(self.my_list.size == 2)
        self.assertTrue(self.my_list.head.data == 1)
        self.assertTrue(self.my_list.head.next_node.data == 2)
        self.assertTrue(self.my_list.head.next_node.next_node == None)

if __name__ == '__main__':
    unittest.main()