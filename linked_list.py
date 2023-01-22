class Node:
    def __init__(self, data): 
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        curr = self.head
        res = "Size: {}, Nodes: ".format(self.size)

        while curr != None:
            res += "{}".format(curr.data)
            curr = curr.next_node
            if curr:
                res += " -> "

        return res

    def append_new(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

        self.size += 1

    def insert_at_pos(self, data, pos):
        if self.size <= pos:
            return False
        else:
            new_node = Node(data)
            curr = self.head
            for _ in range(pos):
                curr = curr.next_node
            new_node.next_node = curr.next_node
            curr.next_node = new_node
            self.size += 1

my_list = LinkedList()
my_list.append_new(1)
my_list.append_new(2)
my_list.append_new(3)
my_list.insert_at_pos(4, 1)
my_list.insert_at_pos(5, 3)
print(my_list)