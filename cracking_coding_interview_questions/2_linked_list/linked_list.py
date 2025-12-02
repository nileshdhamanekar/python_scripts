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
        pointer = self.root
        while pointer is not None:
            print(pointer.value)
            pointer = pointer.next

    def list_size(self):
        pointer = self.root
        count = 0
        while pointer != None:
            count += 1
            pointer = pointer.next
        print(count)

    def delete_node(self, value):
        previous = self.root
        current = self.root
        while current is not None or current != value:
            print("current:{0}".format(current.value))
            if current.value != value:
                previous = current
                current = current.next
            elif current.value == value:
                print("Found")
                previous.next = current.next
                break
        else:
            print("Node not found")


ll = LinkedList()
ll.list_size()
ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.list_size()
ll.print_list()
print('*'*50)
ll.delete_node(20)
ll.print_list()
ll.list_size()
