class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def add_node(self, value):
        node = Node(value)
        node.next = self.root
        self.root = node

    def print_list(self):
        current_node = self.root
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def remove_duplicate(self):
        unique_list = list()
        current_node = self.root
        previous_node = self.root
        while current_node is not None:
            if current_node.value in unique_list:
                previous_node.next = current_node.next
                del current_node
                current_node = previous_node.next
            else:
                unique_list.append(current_node.value)
                previous_node = current_node
                current_node = current_node.next


ll = LinkedList()
ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.add_node(10)
ll.print_list()
print('*'*50)
ll.remove_duplicate()
ll.print_list()