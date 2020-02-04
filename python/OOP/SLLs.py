class SList:
        def __init__(self):
            self.head = None

        def add_to_front(self, val):
            new_node = SLNode(val)
            current_head = self.head
            new_node.next = current_head
            self.head = new_node
            return self

class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

sll = SList()
node1= SLNode("a")