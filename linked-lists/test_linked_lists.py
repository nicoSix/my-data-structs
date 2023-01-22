import unittest
import linked_lists

class TestSinglyLinkedList(unittest.TestCase):
    def test_append(self):
        my_list = linked_lists.SinglyLinkedList()
        my_list.append_new(1)
        my_list.append_new(2)
        self.assertTrue(my_list.head.data == 1)
        self.assertTrue(my_list.head.next_node.data == 2)

if __name__ == '__main__':
    unittest.main()