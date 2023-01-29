class Node:
    """Basic implementation of nodes constituting the singly LinkedList
    """
    def __init__(self, data): 
        self.data = data
        self.next_node = None

    def __str__(self):
        res = "Node value: {}".format(self.data)

        return res

class NodeWithPP(Node):
    """Node that also includes a previous_node pointer, for doubly LinkedList

    Args:
        Node (class): Basic node
    """
    def __init__(self, data):
        self.previous_node = None
        super().__init__(data)
    
class LinkedList:
    """Basic implementation of LinkedList for Python with methods for both singly and doubly LL
    """
    def __init__(self):
        """Creates an empty LinkedList with pointers set to None
        """
        self.head = None
        self.size = 0

    def get_head(self):
        return self.head

    def get_nodes_values_arr(self):
        arr = []
        curr = self.head

        while curr != None:
            arr.append(curr.data)
            curr = curr.next_node

        return arr

    def append_new(self, data, new_node):
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

        self.size += 1

    def get_node_at_pos(self, pos):
        if self.size == 0 or pos >= self.size or pos < 0:
            return False
        else:
            curr = self.head
            for _ in range(pos):
                curr = curr.next_node
            return curr

class SinglyLinkedList(LinkedList):
    """Basic implementation of singly linked list
    """
    def __str__(self):
        res = "Size: {}, Nodes: ".format(self.size)
        res += " -> ".join(str(x) for x in self.get_nodes_values_arr())

        return res

    def append_new(self, data):
        new_node = Node(data)
        super().append_new(data, new_node)

    def insert_at_pos(self, data, pos):
        if pos >= self.size or pos < 0:
            return False

        new_node = Node(data)
        self.size += 1

        if pos == 0:
            head_next = self.get_node_at_pos(pos)
            self.head = new_node
            self.head.next_node = head_next
        else:
            curr = self.get_node_at_pos(pos)
            new_node.next_node = curr.next_node
            curr.next_node = new_node
            
            return curr != None

    def remove_at_pos(self, pos):
        if self.size == 0 or pos >= self.size or pos < 0:
            return False

        if self.size == 1:
            self.size = 0
            self.head = None

        if pos == 0:
            self.head = self.head.next_node
        elif pos == self.size - 1:
            prev_n = self.get_node_at_pos(pos - 1)
            prev_n.next_node = None
        else:
            prev_n = self.get_node_at_pos(pos - 1)
            next_n = self.get_node_at_pos(pos + 1)
            prev_n.next_node = next_n

        self.size -= 1

"""
class DoublyLinkedList(LinkedList):
    def __init__(self):
        self.tail = None
        super().__init__()

    def __str__(self):
        res = "Size: {}, Nodes: ".format(self.size)
        res += " <-> ".join(str(x) for x in self.get_nodes_values_arr())

        return res

    def append_new(self, data):
        new_node = NodeWithPP(data)
        super().append_new(data, new_node)
    
    def insert_at_pos(self, data, pos):
        curr = self.get_node_at_pos(pos)
        if curr:
            new_node = NodeWithPP(data)
            new_node.next_node = curr.next_node
            new_node.previous_node = curr
            
            if curr.next_node:
                curr.next_node.previous_node = new_node
            curr.next_node = new_node
            self.size += 1
        else:
            return False
"""